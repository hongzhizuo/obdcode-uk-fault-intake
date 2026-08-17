#!/usr/bin/env python3
"""Merge this checkout into ~/.cursor/mcp.json and run the MCP self-test."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "show_lamps_mcp.py"
MCP_PATH = Path.home() / ".cursor" / "mcp.json"
KEY = "obdcode-uk-dashboard-lamps"


def main() -> int:
    if sys.version_info < (3, 10):
        print("python 3.10+ required", file=sys.stderr)
        return 1
    if not SCRIPT.is_file():
        print(f"missing {SCRIPT}", file=sys.stderr)
        return 1
    test = subprocess.run(
        [sys.executable, str(SCRIPT), "--self-test"],
        check=False,
    )
    if test.returncode != 0:
        return test.returncode
    MCP_PATH.parent.mkdir(parents=True, exist_ok=True)
    data: dict = {}
    if MCP_PATH.is_file():
        data = json.loads(MCP_PATH.read_text() or "{}")
        if not isinstance(data, dict):
            print(f"{MCP_PATH} is not a JSON object", file=sys.stderr)
            return 1
    servers = data.setdefault("mcpServers", {})
    if not isinstance(servers, dict):
        print("mcpServers must be an object", file=sys.stderr)
        return 1
    servers[KEY] = {
        "command": sys.executable,
        "args": ["-u", str(SCRIPT)],
        "env": {"OBDCODE_IMAGE_MIME": "png"},
    }
    # Drop the old key if a previous install used the repo slug as the server name.
    servers.pop("obdcode-uk-fault-intake", None)
    MCP_PATH.write_text(json.dumps(data, indent=2) + "\n")
    print(f"ok mcp={MCP_PATH} key={KEY} script={SCRIPT}")
    print("Reload MCP, then start a new Agent chat.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
