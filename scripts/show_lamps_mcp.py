#!/usr/bin/env python3
"""Serve the numbered cluster PNG over MCP.

show_dashboard requires board=. It returns ImageContent. Spec hosts get
mimeType image/png. Cursor 3.11 concatenates data:image/${mimeType}, so
set OBDCODE_IMAGE_MIME=png (see scripts/install_mcp.py) on that host.
open_resource is optional Cursor fallback, not required.
"""
from __future__ import annotations

import base64
import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SERVER_NAME = "obdcode-uk-dashboard-lamps"
SERVER_VERSION = "2.0.0"
PROTOCOL_FALLBACK = "2025-03-26"
SUPPORTED_PROTOCOLS = frozenset({
    "2024-11-05",
    "2025-03-26",
    "2025-06-18",
    "2026-07-28",
})
PREVIEW_PNG = Path.home() / ".cursor" / "obdcode-uk-dashboard.png"
PREVIEW_LAMP = Path.home() / ".cursor" / "obdcode-uk-lamp.png"
SPEC_IMG_MIME = "image/png"
CURSOR_IMG_MIME = "png"
LAMP_IDS = (
    "oil-pressure",
    "coolant-temp",
    "brake-system",
    "airbag-srs",
    "power-steering",
    "engine-steady",
    "engine-flashing",
    "battery-charging",
    "dpf",
    "tyre-pressure",
    "abs",
    "esc-traction",
    "glow-plug",
)

LAMPS: dict[int, tuple[str, str]] = {
    1: ("oil-pressure", "lamp-01-oil-pressure.png"),
    2: ("coolant-temp", "lamp-02-coolant-temp.png"),
    3: ("brake-system", "lamp-03-brake-system.png"),
    4: ("airbag-srs", "lamp-04-airbag-srs.png"),
    5: ("power-steering", "lamp-05-power-steering.png"),
    6: ("engine-steady", "lamp-06-engine-steady.png"),
    7: ("engine-flashing", "lamp-07-engine-flashing.png"),
    8: ("battery-charging", "lamp-08-battery-charging.png"),
    9: ("dpf", "lamp-09-dpf.png"),
    10: ("tyre-pressure", "lamp-10-tyre-pressure.png"),
    11: ("abs", "lamp-11-abs.png"),
    12: ("esc-traction", "lamp-12-esc-traction.png"),
    13: ("glow-plug", "lamp-13-glow-plug.png"),
}
ID_TO_NUMBER = {lamp_id: n for n, (lamp_id, _) in LAMPS.items()}
BOARDS = {
    "unknown": "cluster.png",
    "petrol": "cluster-petrol.png",
    "diesel": "cluster-diesel.png",
    "hybrid": "cluster-hybrid.png",
    "electric": "cluster-electric.png",
}
BOARD_CAPTIONS = {
    "unknown": (
        "Use the circled number on this picture, not a count. "
        "If it flashes, say flashing."
    ),
    "petrol": (
        "Petrol picture. Empty slots are not on this car and have no "
        "circled number. Pick 9 or exhaust-dots: unmatched-gpf, not DPF."
    ),
    "diesel": (
        "Diesel picture. 9 is DPF. 13 is only a fault if it stays on or "
        "flashes after start. AdBlue is not drawn — they should say AdBlue."
    ),
    "hybrid": (
        "Hybrid picture. Engine and 12V still apply. Pick 9 or exhaust-dots: "
        "unmatched-gpf, not DPF."
    ),
    "electric": (
        "Electric picture. 8 is the 12V rectangle only. Turtle, car-with-!, "
        "or a charge plug: unmatched-ev — do not pick 12 or 8."
    ),
}

_client_name = ""


def image_mime() -> str:
    env = (os.environ.get("OBDCODE_IMAGE_MIME") or "").strip().lower()
    if env in {CURSOR_IMG_MIME, SPEC_IMG_MIME}:
        return env
    if "cursor" in _client_name.lower():
        return CURSOR_IMG_MIME
    return SPEC_IMG_MIME


TOOLS = [
    {
        "name": "show_dashboard",
        "description": (
            "Return this car's numbered dashboard PNG. board is required: "
            "petrol|diesel|hybrid|electric|unknown from fuel_type and fuel_raw. "
            "Empty args is a fail, not the full 13-lamp picture. Ask which "
            "circled number matches the lit shape. Do not list lamp names. "
            "Do not ask if they are driving."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "board": {
                    "type": "string",
                    "enum": ["petrol", "diesel", "hybrid", "electric", "unknown"],
                    "description": "Required. unknown only when lookup failed and fuel is still unknown.",
                },
                "body": {
                    "type": "string",
                    "enum": ["car", "van"],
                    "description": "Speech only. Same PNG as the fuel board. Prefer saying your Transit, not van board.",
                },
            },
            "required": ["board"],
            "additionalProperties": False,
        },
    },
    {
        "name": "show_lamp",
        "description": (
            "Optional confirm PNG for one lamp after a valid pick. Skip unless "
            "they hesitate. Pass number 1-13 or id from the 13-lamp enum."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "minimum": 1, "maximum": 13},
                "id": {"type": "string", "enum": list(LAMP_IDS)},
            },
            "additionalProperties": False,
        },
    },
]


def log(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


def png_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def publish_preview(src: Path, dest: Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    return dest.resolve().as_uri()


def picture(path: Path, caption: str, dest: Path) -> dict:
    preview = publish_preview(path, dest)
    data = png_b64(path)
    mime = image_mime()
    return {
        "content": [
            {
                "type": "image",
                "data": data,
                "mimeType": mime,
                "annotations": {"audience": ["user", "assistant"], "priority": 1.0},
            },
            {
                "type": "resource",
                "resource": {
                    "uri": preview,
                    "mimeType": SPEC_IMG_MIME,
                    "blob": data,
                },
            },
            {
                "type": "text",
                "text": (
                    f"{caption} If the owner cannot see the picture, say so. "
                    f"Optional Cursor preview URI: {preview}."
                ),
                "annotations": {"audience": ["user", "assistant"]},
            },
        ]
    }


def error_content(message: str) -> dict:
    return {"content": [{"type": "text", "text": message}], "isError": True}


def resolve_lamp(args: dict | None) -> tuple[int, str, Path] | str:
    args = args or {}
    number = args.get("number")
    lamp_id = str(args.get("id") or "").strip().lower()
    if number is None and lamp_id:
        if lamp_id not in ID_TO_NUMBER:
            return f"Unknown lamp id {lamp_id!r}. Use 1-13 or a listed id."
        number = ID_TO_NUMBER[lamp_id]
    try:
        number = int(number)
    except (TypeError, ValueError):
        return "Pass number (1-13) or id."
    if number not in LAMPS:
        return "Lamp number must be 1-13."
    lamp_id, filename = LAMPS[number]
    path = ASSETS / filename
    if not path.is_file():
        return f"Missing {path}"
    return number, lamp_id, path


def cluster_path(board: str) -> Path | None:
    name = BOARDS.get(board)
    if not name:
        return None
    path = ASSETS / name
    if path.is_file():
        return path
    return None


def dashboard_caption(board: str, body: str) -> str:
    text = BOARD_CAPTIONS.get(board, BOARD_CAPTIONS["unknown"])
    if body == "van":
        return f"Same {board} picture. Call it your van, not a van board. {text}"
    return text


def resource_entries() -> list[dict]:
    out = []
    for board, filename in BOARDS.items():
        path = ASSETS / filename
        if path.is_file():
            out.append({
                "uri": path.resolve().as_uri(),
                "name": f"cluster-{board}",
                "mimeType": SPEC_IMG_MIME,
            })
    return out


def read_resource(uri: str) -> dict | str:
    wanted = {e["uri"]: e["name"] for e in resource_entries()}
    if uri not in wanted:
        preview = PREVIEW_PNG.resolve().as_uri()
        if uri == preview and PREVIEW_PNG.is_file():
            return {
                "contents": [{
                    "uri": uri,
                    "mimeType": SPEC_IMG_MIME,
                    "blob": png_b64(PREVIEW_PNG),
                }]
            }
        return f"Unknown resource {uri}"
    path = Path(uri.removeprefix("file://"))
    if not path.is_file():
        return f"Missing {path}"
    return {
        "contents": [{
            "uri": uri,
            "mimeType": SPEC_IMG_MIME,
            "blob": png_b64(path),
        }]
    }


def call_tool(name: str, args: dict | None) -> dict:
    args = args or {}
    if name == "show_dashboard":
        raw = args.get("board")
        if raw is None or str(raw).strip() == "":
            return error_content(
                "board is required (petrol|diesel|hybrid|electric|unknown). "
                "Empty args is a fail — do not show the full 13-lamp picture."
            )
        board = str(raw).strip().lower()
        if board not in BOARDS:
            return error_content(
                f"Unknown board {board!r}. Use petrol|diesel|hybrid|electric|unknown."
            )
        body = str(args.get("body") or "car").strip().lower()
        if body not in {"car", "van"}:
            body = "car"
        path = cluster_path(board)
        if path is None:
            return error_content(
                f"Missing cluster PNG for board {board!r}. Do not substitute another board."
            )
        return picture(path, dashboard_caption(board, body), PREVIEW_PNG)
    if name == "show_lamp":
        resolved = resolve_lamp(args)
        if isinstance(resolved, str):
            return error_content(resolved)
        number, lamp_id, path = resolved
        return picture(path, f"Lamp {number} ({lamp_id}).", PREVIEW_LAMP)
    return error_content(f"Unknown tool {name}")


def handle(msg: dict) -> dict | None:
    global _client_name
    method = msg.get("method")
    req_id = msg.get("id")
    params = msg.get("params") or {}

    if method in {"notifications/initialized", "notifications/cancelled"}:
        return None
    if method is None:
        return None

    if method == "initialize":
        offered = params.get("protocolVersion") or PROTOCOL_FALLBACK
        version = offered if offered in SUPPORTED_PROTOCOLS else PROTOCOL_FALLBACK
        info = params.get("clientInfo") or {}
        _client_name = str(info.get("name") or "")
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": version,
                "capabilities": {"tools": {}, "resources": {}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                "instructions": (
                    "board is required on show_dashboard. Classify from "
                    "fuel_type and fuel_raw. The tool returns the PNG; ask "
                    "which circled number is lit. Do not list lamp names. "
                    "Do not ask if they are driving. Vans: same PNG, say "
                    "your Transit. Petrol/hybrid 9 is unmatched-gpf."
                ),
            },
        }

    if method == "ping":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}}

    if method == "tools/call":
        name = params.get("name") or ""
        args = params.get("arguments") or {}
        return {"jsonrpc": "2.0", "id": req_id, "result": call_tool(name, args)}

    if method == "resources/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"resources": resource_entries()},
        }

    if method == "resources/read":
        uri = str((params or {}).get("uri") or "")
        got = read_resource(uri)
        if isinstance(got, str):
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32002, "message": got},
            }
        return {"jsonrpc": "2.0", "id": req_id, "result": got}

    if method in {"prompts/list", "resources/templates/list"}:
        key = "resourceTemplates" if "templates" in method else "prompts"
        return {"jsonrpc": "2.0", "id": req_id, "result": {key: []}}

    if req_id is None:
        return None
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


class FramedIO:
    def __init__(self) -> None:
        self.mode: str | None = None

    def read(self) -> dict | None:
        header = sys.stdin.buffer.readline()
        if not header:
            return None
        if header.lower().startswith(b"content-length:"):
            self.mode = "lsp"
            length = int(header.split(b":", 1)[1])
            while True:
                line = sys.stdin.buffer.readline()
                if line in (b"", b"\n", b"\r\n"):
                    break
                if line.lower().startswith(b"content-length:"):
                    length = int(line.split(b":", 1)[1])
            body = sys.stdin.buffer.read(length)
            return json.loads(body.decode("utf-8"))
        self.mode = "ndjson"
        line = header
        while line in (b"\n", b"\r\n"):
            line = sys.stdin.buffer.readline()
            if not line:
                return None
        return json.loads(line.decode("utf-8"))

    def write(self, msg: dict) -> None:
        body = json.dumps(msg, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        if self.mode == "lsp":
            sys.stdout.buffer.write(
                f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
            )
            sys.stdout.buffer.write(body)
        else:
            sys.stdout.buffer.write(body + b"\n")
        sys.stdout.buffer.flush()


def serve() -> None:
    io = FramedIO()
    while True:
        try:
            msg = io.read()
        except Exception as exc:
            log(f"bad message: {exc}")
            continue
        if msg is None:
            return
        try:
            reply = handle(msg)
        except Exception as exc:
            log(f"handle failed: {exc}")
            if "id" in msg:
                io.write({
                    "jsonrpc": "2.0",
                    "id": msg.get("id"),
                    "error": {"code": -32603, "message": str(exc)},
                })
            continue
        if reply is not None:
            io.write(reply)


def self_test() -> int:
    missing = call_tool("show_dashboard", {})
    if not missing.get("isError"):
        print("FAIL empty board should error", file=sys.stderr)
        return 1
    for board, filename in BOARDS.items():
        path = ASSETS / filename
        if not path.is_file():
            print(f"FAIL missing {filename}", file=sys.stderr)
            return 1
        result = call_tool("show_dashboard", {"board": board})
        if result.get("isError"):
            print(f"FAIL {board} {result}", file=sys.stderr)
            return 1
        image = result["content"][0]
        if image["type"] != "image" or image["mimeType"] != SPEC_IMG_MIME:
            print(f"FAIL {board} default mime {image.get('mimeType')}", file=sys.stderr)
            return 1
        raw = base64.b64decode(image["data"])
        if raw[:8] != b"\x89PNG\r\n\x1a\n":
            print(f"FAIL {board} not png", file=sys.stderr)
            return 1
        if path.read_bytes() != raw:
            print(f"FAIL {board} bytes mismatch", file=sys.stderr)
            return 1
        text = result["content"][-1]["text"]
        if "Circled numbers on this picture" in text:
            print(f"FAIL {board} dumped number list", file=sys.stderr)
            return 1
        if "open_resource" in text.lower():
            print(f"FAIL {board} required open_resource", file=sys.stderr)
            return 1
    os.environ["OBDCODE_IMAGE_MIME"] = CURSOR_IMG_MIME
    cursor = call_tool("show_dashboard", {"board": "petrol"})
    if cursor["content"][0]["mimeType"] != CURSOR_IMG_MIME:
        print("FAIL cursor mime override", file=sys.stderr)
        return 1
    del os.environ["OBDCODE_IMAGE_MIME"]
    van = call_tool("show_dashboard", {"board": "diesel", "body": "van"})
    text = van["content"][-1]["text"]
    if "Van board" in text:
        print("FAIL old van-board caption", file=sys.stderr)
        return 1
    if "your van" not in text.lower() and "Transit" not in text:
        if "same diesel picture" not in text.lower():
            print(f"FAIL van caption {text!r}", file=sys.stderr)
            return 1
    petrol = call_tool("show_dashboard", {"board": "petrol"})
    if "unmatched-gpf" not in petrol["content"][-1]["text"]:
        print("FAIL petrol caption missing unmatched-gpf", file=sys.stderr)
        return 1
    if not PREVIEW_PNG.is_file():
        print("FAIL preview missing", file=sys.stderr)
        return 1
    listed = resource_entries()
    if len(listed) != len(BOARDS):
        print(f"FAIL resources {len(listed)}", file=sys.stderr)
        return 1
    print(f"ok preview={PREVIEW_PNG} boards={len(BOARDS)} mime_default={SPEC_IMG_MIME}")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    serve()
