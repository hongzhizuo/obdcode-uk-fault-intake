#!/usr/bin/env python3
"""Stdio MCP server: put the dashboard into the owner's Cursor chat.

Two channels, because Cursor treats them differently:

1. MCP Apps (SEP-1865): tool _meta.ui.resourceUri + ui:// HTML resource.
   Cursor 2.6+ can render that HTML as an iframe in the conversation.
   Pattern copied from modelcontextprotocol/ext-apps examples/qr-server.
2. ImageContent on the tool result, for hosts that show images but not Apps.

Read-tool PNGs and markdown ![] never reach the owner. Exploring SKILL.md
is not showing the picture.

No third-party packages. NDJSON and Content-Length framing. Logs to stderr.
"""
from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SERVER_NAME = "obdcode-uk-fault-intake"
SERVER_VERSION = "1.1.0"
PROTOCOL_FALLBACK = "2025-03-26"
SUPPORTED_PROTOCOLS = frozenset({
    "2024-11-05",
    "2025-03-26",
    "2025-06-18",
    "2026-07-28",
})
APP_MIME = "text/html;profile=mcp-app"
DASHBOARD_URI = "ui://obdcode-uk-fault-intake/dashboard.html"
LAMP_URI = "ui://obdcode-uk-fault-intake/lamp.html"
SDK_SRC = "https://unpkg.com/@modelcontextprotocol/ext-apps@0.4.0/app-with-deps"
UI_CSP = {"csp": {"resourceDomains": ["https://unpkg.com"]}}

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


def ui_meta(uri: str) -> dict:
    return {"ui": {"resourceUri": uri}, "ui/resourceUri": uri}


TOOLS = [
    {
        "name": "show_dashboard",
        "description": (
            "REQUIRED first call when the owner gives a UK plate or mentions a "
            "warning lamp and has not picked a number yet. Renders the numbered "
            "instrument cluster as an MCP App in THEIR chat. Do not Explore "
            "SKILL.md instead of this. Do not say 'look at the picture above' "
            "unless you have called this tool in this turn."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
        "_meta": ui_meta(DASHBOARD_URI),
    },
    {
        "name": "show_lamp",
        "description": (
            "Show one dashboard lamp in the user's chat so they can confirm "
            "the shape. Pass the number printed on the cluster (1-13)."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "number": {"type": "integer", "minimum": 1, "maximum": 13},
                "id": {"type": "string"},
            },
            "additionalProperties": False,
        },
        "_meta": ui_meta(LAMP_URI),
    },
]


def log(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


def png_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


DASHBOARD_HTML = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="color-scheme" content="dark">
  <style>
    html, body { margin: 0; padding: 12px; background: #111; color: #ececf0;
      font-family: ui-sans-serif, system-ui, sans-serif; }
    img { width: 100%; max-width: 880px; display: block; border-radius: 10px; }
    .hint { font-size: 13px; color: #b0b2b8; margin: 10px 0 8px; }
    .row { display: flex; flex-wrap: wrap; gap: 6px; }
    button { min-width: 40px; height: 36px; border-radius: 8px; cursor: pointer;
      border: 1px solid #3a3c44; background: #1c1d22; color: #fff; font-size: 14px; }
    button:hover, button.sel { background: #2a2c34; border-color: #6a6e7a; }
    #status { font-size: 12px; color: #8a8d96; margin-top: 8px; min-height: 1em; }
  </style>
</head>
<body>
  <img id="cluster" alt="Your dashboard" src="data:image/png;base64,CLUSTER_B64">
  <p class="hint">Match the shape that is lit. Tap the number. If it flashes, tap flashing then the number — or tap 7 for the flashing engine lamp.</p>
  <div class="row" id="nums"></div>
  <div id="status"></div>
  <script type="module">
    const nums = document.getElementById("nums");
    const status = document.getElementById("status");
    for (let n = 1; n <= 13; n++) {
      const b = document.createElement("button");
      b.type = "button";
      b.textContent = String(n);
      b.addEventListener("click", () => pick(n, b));
      nums.appendChild(b);
    }
    let app = null;
    try {
      const { App } = await import("SDK_SRC");
      app = new App({ name: "OBDCode dashboard", version: "1.1.0" });
      app.ontoolresult = ({ content }) => {
        const img = content && content.find(c => c.type === "image");
        if (img && img.data) {
          document.getElementById("cluster").src =
            "data:" + (img.mimeType || "image/png") + ";base64," + img.data;
        }
      };
      await app.connect();
    } catch (err) {
      status.textContent = "Picture is on screen. Type the number in chat if tap does not send.";
    }
    async function pick(n, btn) {
      for (const el of nums.querySelectorAll("button")) el.classList.remove("sel");
      btn.classList.add("sel");
      const text = String(n);
      status.textContent = "Picked " + text + ".";
      try {
        if (app && typeof app.sendMessage === "function") {
          await app.sendMessage({ role: "user", content: [{ type: "text", text }] });
          return;
        }
        if (app && typeof app.updateModelContext === "function") {
          await app.updateModelContext({
            content: [{ type: "text", text: "Owner picked lamp " + text }]
          });
        }
      } catch (err) {
        status.textContent = "Picked " + text + ". Type that number in the chat.";
      }
    }
  </script>
</body>
</html>
""".replace("SDK_SRC", SDK_SRC)

LAMP_HTML = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="color-scheme" content="dark">
  <style>
    html, body { margin: 0; padding: 16px; background: #111; color: #ececf0;
      font-family: ui-sans-serif, system-ui, sans-serif; text-align: center; }
    img { width: 180px; height: 180px; }
    p { font-size: 13px; color: #b0b2b8; }
  </style>
</head>
<body>
  <div id="pic"></div>
  <p id="cap">Confirm this is the lamp that is lit.</p>
  <script type="module">
    import { App } from "SDK_SRC";
    const app = new App({ name: "OBDCode lamp", version: "1.1.0" });
    app.ontoolresult = ({ content }) => {
      const img = content && content.find(c => c.type === "image");
      const text = content && content.find(c => c.type === "text");
      if (img && img.data) {
        const image = document.createElement("img");
        image.alt = "Lamp";
        image.src = "data:" + (img.mimeType || "image/png") + ";base64," + img.data;
        const pic = document.getElementById("pic");
        pic.innerHTML = "";
        pic.appendChild(image);
      }
      if (text && text.text) document.getElementById("cap").textContent = text.text;
    };
    await app.connect();
  </script>
</body>
</html>
""".replace("SDK_SRC", SDK_SRC)


def dashboard_html() -> str:
    path = ASSETS / "cluster.png"
    return DASHBOARD_HTML.replace("CLUSTER_B64", png_b64(path))


def png_content(path: Path, caption: str, uri: str) -> dict:
    data = png_b64(path)
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
        ],
        "_meta": ui_meta(uri),
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
            DASHBOARD_URI,
        )
    if name == "show_lamp":
        resolved = resolve_lamp(args)
        if isinstance(resolved, str):
            return error_content(resolved)
        number, lamp_id, path = resolved
        return png_content(path, f"Lamp {number} ({lamp_id}).", LAMP_URI)
    return error_content(f"Unknown tool {name}")


def resource_list() -> list[dict]:
    return [
        {
            "uri": DASHBOARD_URI,
            "name": "dashboard",
            "title": "Your dashboard",
            "mimeType": APP_MIME,
            "_meta": {"ui": UI_CSP},
        },
        {
            "uri": LAMP_URI,
            "name": "lamp",
            "title": "One lamp",
            "mimeType": APP_MIME,
            "_meta": {"ui": UI_CSP},
        },
    ]


def resource_read(uri: str) -> dict:
    if uri == DASHBOARD_URI:
        text = dashboard_html()
    elif uri == LAMP_URI:
        text = LAMP_HTML
    else:
        return {
            "jsonrpc": "2.0",
            "error": {"code": -32602, "message": f"Unknown resource {uri}"},
        }
    return {
        "contents": [
            {
                "uri": uri,
                "mimeType": APP_MIME,
                "text": text,
                "_meta": {"ui": UI_CSP},
            }
        ]
    }


def handle(msg: dict) -> dict | None:
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
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": version,
                "capabilities": {
                    "tools": {},
                    "resources": {},
                    "extensions": {
                        "io.modelcontextprotocol/ui": {"mimeTypes": [APP_MIME]}
                    },
                },
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                "instructions": (
                    "When the owner gives a UK plate and has not picked a lamp, "
                    "call show_dashboard in that same turn so the MCP App iframe "
                    "appears in THEIR chat. Exploring markdown is not the picker. "
                    "After they pick a number, call show_lamp."
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
        return {"jsonrpc": "2.0", "id": req_id, "result": {"resources": resource_list()}}

    if method == "resources/templates/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"resourceTemplates": []}}

    if method == "resources/read":
        uri = params.get("uri") or ""
        payload = resource_read(uri)
        if "error" in payload and "contents" not in payload:
            payload["id"] = req_id
            payload["jsonrpc"] = "2.0"
            return payload
        return {"jsonrpc": "2.0", "id": req_id, "result": payload}

    if method == "prompts/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"prompts": []}}

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
    cluster = ASSETS / "cluster.png"
    if not cluster.is_file():
        print("FAIL missing cluster.png", file=sys.stderr)
        return 1
    result = call_tool("show_dashboard", {})
    if result.get("_meta", {}).get("ui", {}).get("resourceUri") != DASHBOARD_URI:
        print("FAIL tool result missing ui.resourceUri", file=sys.stderr)
        return 1
    html = dashboard_html()
    if "CLUSTER_B64" in html or "data:image/png;base64," not in html:
        print("FAIL dashboard html not baked", file=sys.stderr)
        return 1
    listed = handle({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
    dash = listed["result"]["tools"][0]
    if dash["_meta"]["ui"]["resourceUri"] != DASHBOARD_URI:
        print("FAIL tools/list missing ui meta", file=sys.stderr)
        return 1
    init = handle({
        "jsonrpc": "2.0", "id": 2, "method": "initialize",
        "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "t", "version": "0"}},
    })
    ext = init["result"]["capabilities"]["extensions"]["io.modelcontextprotocol/ui"]
    if APP_MIME not in ext["mimeTypes"]:
        print("FAIL initialize missing ui extension", file=sys.stderr)
        return 1
    res = handle({"jsonrpc": "2.0", "id": 3, "method": "resources/read", "params": {"uri": DASHBOARD_URI}})
    body = res["result"]["contents"][0]
    if body["mimeType"] != APP_MIME:
        print("FAIL resource mime", file=sys.stderr)
        return 1
    raw_b64 = body["text"].split("base64,", 1)[1].split('"', 1)[0]
    raw = base64.b64decode(raw_b64 + "=" * (-len(raw_b64) % 4))
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        print("FAIL baked image is not PNG", file=sys.stderr)
        return 1
    print(f"ok mcp-app dashboard_html={len(html)}B uri={DASHBOARD_URI}")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    serve()
