# -*- coding: utf-8 -*-
"""QGIS Python console smoke test for the connectivity bridge.

Paste or run this script inside the QGIS Python console.
"""

import json
import sys

BRIDGE_ROOT = r"C:\IGP\versiones_laptop\ref_princip_laptop\connectivity_bridge_test"

if BRIDGE_ROOT not in sys.path:
    sys.path.insert(0, BRIDGE_ROOT)

print("Bridge root agregado a sys.path: {0}".format(BRIDGE_ROOT))

from connectivity_bridge.public_api import open_connectivity_dialog, test_import

import_result = test_import()
print("test_import():")
print(json.dumps(import_result, indent=2, ensure_ascii=False))

dialog_result = open_connectivity_dialog(iface=iface)
print("open_connectivity_dialog(iface=iface):")
print(json.dumps(dialog_result, indent=2, ensure_ascii=False))

