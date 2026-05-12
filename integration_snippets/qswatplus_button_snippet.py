# -*- coding: utf-8 -*-
"""Snippet no invasivo para agregar un boton temporal en QSWATPlus IGP.

No ejecutar este archivo directamente. Es una guia para copiar/adaptar dentro del
punto de registro de acciones del plugin, por ejemplo initGui().
"""


def add_connectivity_bridge_action(self):
    """Ejemplo para pegar/adaptar dentro de la clase principal del plugin."""
    import sys

    from qgis.PyQt.QtWidgets import QAction, QMessageBox

    bridge_root = r"C:\IGP\versiones_laptop\ref_princip_laptop\connectivity_bridge_test"
    if bridge_root not in sys.path:
        sys.path.insert(0, bridge_root)

    self._connectivity_bridge_action = QAction(
        "Probar modulo de conectividad sedimentaria",
        self._iface.mainWindow(),
    )

    def _run_connectivity_bridge_test():
        try:
            from connectivity_bridge.public_api import (
                open_connectivity_dialog,
                test_import,
            )

            import_result = test_import()
            if not import_result.get("ok"):
                QMessageBox.warning(
                    self._iface.mainWindow(),
                    "Conectividad sedimentaria",
                    "No se pudo importar el bridge:\n{0}".format(
                        import_result.get("message", "Error sin detalle")
                    ),
                )
                return

            dialog_result = open_connectivity_dialog(
                iface=self._iface,
                parent=self._iface.mainWindow(),
            )
            if not dialog_result.get("ok"):
                QMessageBox.warning(
                    self._iface.mainWindow(),
                    "Conectividad sedimentaria",
                    dialog_result.get("message", "No se pudo abrir la ventana."),
                )
        except Exception as exc:
            QMessageBox.critical(
                self._iface.mainWindow(),
                "Conectividad sedimentaria",
                "Error invocando connectivity_bridge:\n{0}".format(exc),
            )

    self._connectivity_bridge_action.triggered.connect(_run_connectivity_bridge_test)

    # Adaptar el nombre del menu al usado por el plugin IGP si difiere.
    self._iface.addToolBarIcon(self._connectivity_bridge_action)
    self._iface.addPluginToMenu("&QSWAT+", self._connectivity_bridge_action)


def remove_connectivity_bridge_action(self):
    """Ejemplo para pegar/adaptar dentro de unload()."""
    try:
        self._iface.removePluginMenu("&QSWAT+", self._connectivity_bridge_action)
        self._iface.removeToolBarIcon(self._connectivity_bridge_action)
    except Exception:
        pass

