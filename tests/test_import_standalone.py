# -*- coding: utf-8 -*-
"""Standalone import smoke test for connectivity_bridge.

Run from the bridge root:
    python tests\test_import_standalone.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    bridge_root = Path(__file__).resolve().parents[1]
    if str(bridge_root) not in sys.path:
        sys.path.insert(0, str(bridge_root))

    print("Bridge root agregado a sys.path: {0}".format(bridge_root))

    from connectivity_bridge import public_api

    info = public_api.get_module_info()
    import_result = public_api.test_import()

    print("get_module_info():")
    print(json.dumps(info, indent=2, ensure_ascii=False))
    print("test_import():")
    print(json.dumps(import_result, indent=2, ensure_ascii=False))

    if not import_result.get("ok"):
        print("ERROR: test_import() no devolvio ok=True.")
        return 1

    print("OK: import standalone completado correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

