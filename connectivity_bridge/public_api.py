# -*- coding: utf-8 -*-
"""Public API for the sediment connectivity bridge smoke test.

This module intentionally avoids scientific processing and heavy data dependencies.
It only validates that QSWATPlus IGP can import and invoke an external module.
"""

from __future__ import annotations

import traceback
from typing import Any, Dict, Optional


BRIDGE_VERSION = "bridge-test-0.1"
_LAST_DIALOG = None


def get_module_info() -> Dict[str, Any]:
    """Return stable metadata for the bridge module."""
    return {
        "module_name": "Sediment Connectivity Bridge Test",
        "short_name": "connectivity_bridge_test",
        "version": BRIDGE_VERSION,
        "status": "technical-smoke-test",
        "purpose": (
            "Validate import and invocation from QSWATPlus IGP without exposing "
            "the scientific runner."
        ),
        "runs_scientific_engine": False,
    }


def test_import() -> Dict[str, Any]:
    """Confirm that the bridge package can be imported."""
    try:
        info = get_module_info()
        return {
            "ok": True,
            "message": "connectivity_bridge imported successfully.",
            "module_info": info,
        }
    except Exception as exc:
        return {
            "ok": False,
            "message": "Import smoke test failed: {0}".format(exc),
            "traceback": traceback.format_exc(),
        }


def open_connectivity_dialog(
    iface: Optional[Any] = None,
    parent: Optional[Any] = None,
    project_context: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Open a minimal dialog when running inside QGIS/QSWATPlus.

    Outside QGIS this returns a clear diagnostic instead of raising.
    """
    try:
        from .dialog_min import create_connectivity_dialog, is_qgis_pyqt_available

        if not is_qgis_pyqt_available():
            return {
                "ok": False,
                "opened": False,
                "message": (
                    "qgis.PyQt is not available. Run this from QGIS/QSWATPlus "
                    "to open the dialog."
                ),
                "module_info": get_module_info(),
            }

        if parent is None and iface is not None and hasattr(iface, "mainWindow"):
            parent = iface.mainWindow()

        global _LAST_DIALOG
        dialog = create_connectivity_dialog(
            iface=iface,
            parent=parent,
            project_context=project_context,
        )
        _LAST_DIALOG = dialog
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()

        return {
            "ok": True,
            "opened": True,
            "message": "Minimal connectivity bridge dialog opened.",
            "module_info": get_module_info(),
        }
    except Exception as exc:
        return {
            "ok": False,
            "opened": False,
            "message": "Could not open connectivity bridge dialog: {0}".format(exc),
            "traceback": traceback.format_exc(),
            "module_info": get_module_info(),
        }
