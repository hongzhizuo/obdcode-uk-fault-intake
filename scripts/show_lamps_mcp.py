#!/usr/bin/env python3
"""Stdio MCP server: put dashboard lamp pictures into the user's Cursor chat.

Cursor's Read tool shows images to the model, not in the owner's message.
MCP image content does render in the chat. This server exists for that.

No third-party packages. Speaks newline-delimited JSON (Python MCP SDK) and
Content-Length framing (TypeScript MCP SDK). Logs go to stderr only.
"""
from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SERVER_NAME = "obdcode-uk-fault-intake"
SERVER_VERSION = "1.0.0"
PROTOCOL_FALLBACK = "2025-03-26"
SUPPORTED_PROTOCOLS = frozenset({
    "2024-11-05",
    "2025-03-26",
    "2025-06-18",
    "2026-07-28",
})

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

TOOLS = [
    {
        "name": "show_dashboard",
        "description": (
            "Show the numbered UK instrument-cluster picture in the user's chat "
            "so they can match the lamp that is lit on their car. Call this when "
            "they give a plate or mention a warning light and have not yet picked "
            "a lamp. Do not replace this with a text list of lamp names."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "name": "show_lamp",
        "description": (
            "Show one dashboard lamp picture in the user's chat so they can "
            "confirm the shape. Pass the number printed on the cluster (1-13), "
            "or the lamp id such as engine-steady."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "minimum": 1, "maximum": 13},
                "id": {"type": "string"},
            },
            "additionalProperties": False,
        },
    },
]


def log(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


def png_content(path: Path, caption: str) -> dict:
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return {
        "content": [
            {
                "type": "image",
                "data": data,
                "mimeType": "image/png",
                "annotations": {"audience": ["user"], "priority": 1.0},
            },
            {
                "type": "text",
                "text": caption,
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


def call_tool(name: str, args: dict | None) -> dict:
    if name == "show_dashboard":
        path = ASSETS / "cluster.png"
        if not path.is_file():
            return error_content(f"Missing {path}")
        return png_content(
            path,
            "Match the shape that is lit on your car. Reply with the number. "
            "If it flashes, say flashing.",
        )
    if name == "show_lamp":
        resolved = resolve_lamp(args)
        if isinstance(resolved, str):
            return error_content(resolved)
        number, lamp_id, path = resolved
        return png_content(path, f"Lamp {number} ({lamp_id}).")
    return error_content(f"Unknown tool {name}")


def handle(msg: dict) -> dict | None:
    method = msg.get("method")
    req_id = msg.get("id")
    params = msg.get("params") or {}

    if method == "notifications/initialized" or method == "notifications/cancelled":
        return None
    if method is None:
        return None

    if method == "initialize":
        offered = params.get("protocolVersion") or PROTOCOL_FALLBACK
        version = offered if offered in SUPPORTED_PROTOCOLS else PROTOCOL_FALLBACK
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": version,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                "instructions": (
                    "Put the UK dashboard picture in the user's chat with "
                    "show_dashboard. After they pick a number, call show_lamp. "
                    "Do not describe the lamps in prose."
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

    if method in {"resources/list", "prompts/list"}:
        key = "resources" if method.startswith("resources") else "prompts"
        return {"jsonrpc": "2.0", "id": req_id, "result": {key: []}}

    if req_id is None:
        return None
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


class FramedIO:
    """Detect Content-Length vs NDJSON from the first request, then stick to it."""

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
            sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
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
    cluster = ASSETS / "cluster.png"
    if not cluster.is_file():
        print("FAIL missing cluster.png", file=sys.stderr)
        return 1
    result = call_tool("show_dashboard", {})
    image = result["content"][0]
    raw = base64.b64decode(image["data"])
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        print("FAIL cluster is not PNG", file=sys.stderr)
        return 1
    if image.get("annotations", {}).get("audience") != ["user"]:
        print("FAIL image must be audience=user", file=sys.stderr)
        return 1
    lamp = call_tool("show_lamp", {"number": 6})
    raw6 = base64.b64decode(lamp["content"][0]["data"])
    if raw6[:8] != b"\x89PNG\r\n\x1a\n":
        print("FAIL lamp 6 is not PNG", file=sys.stderr)
        return 1
    listed = handle({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
    names = [t["name"] for t in listed["result"]["tools"]]
    if names != ["show_dashboard", "show_lamp"]:
        print(f"FAIL tools {names}", file=sys.stderr)
        return 1
    print(
        f"ok cluster={len(raw)}B lamp6={len(raw6)}B "
        f"dashboard_tool=show_dashboard"
    )
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    serve()
