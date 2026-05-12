# -*- coding: utf-8 -*-
"""Minimal PyQt dialog for the sediment connectivity bridge smoke test."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .public_api import BRIDGE_VERSION


def is_qgis_pyqt_available() -> bool:
    """Return True when qgis.PyQt can be imported."""
    try:
        from qgis.PyQt.QtWidgets import QDialog  # noqa: F401

        return True
    except Exception:
        return False


def _project_label() -> str:
    try:
        from qgis.core import QgsProject

        project_file = QgsProject.instance().fileName()
        if project_file:
            return "Proyecto QGIS activo: {0}".format(project_file)
        return "Proyecto QGIS activo: sin archivo guardado"
    except Exception:
        return "Proyecto QGIS activo: no disponible"


def create_connectivity_dialog(
    iface: Optional[Any] = None,
    parent: Optional[Any] = None,
    project_context: Optional[Dict[str, Any]] = None,
):
    """Create and return the minimal bridge dialog.

    Importing Qt inside the function keeps standalone imports safe outside QGIS.
    """
    from qgis.PyQt.QtCore import Qt
    from qgis.PyQt.QtWidgets import (
        QDialog,
        QFormLayout,
        QLabel,
        QPushButton,
        QVBoxLayout,
    )

    dialog = QDialog(parent)
    dialog.setWindowTitle("Módulo de Conectividad Sedimentaria")
    dialog.setMinimumWidth(480)
    dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    main_layout = QVBoxLayout(dialog)

    title = QLabel("Módulo de Conectividad Sedimentaria")
    title_font = title.font()
    title_font.setBold(True)
    title_font.setPointSize(max(title_font.pointSize() + 2, 10))
    title.setFont(title_font)
    main_layout.addWidget(title)

    message = QLabel("Bridge test cargado correctamente desde QSWATPlus IGP")
    message.setWordWrap(True)
    main_layout.addWidget(message)

    form = QFormLayout()
    form.addRow("Version:", QLabel(BRIDGE_VERSION))
    form.addRow(
        "Estado:",
        QLabel("Prueba de invocación técnica, sin ejecución científica"),
    )
    form.addRow("Proyecto:", QLabel(_project_label()))

    iface_status = "iface recibido" if iface is not None else "iface no recibido"
    form.addRow("Contexto QGIS:", QLabel(iface_status))

    if project_context:
        context_label = QLabel(str(project_context))
        context_label.setWordWrap(True)
        form.addRow("Contexto externo:", context_label)

    main_layout.addLayout(form)

    close_button = QPushButton("Cerrar")
    close_button.clicked.connect(dialog.close)
    main_layout.addWidget(close_button)

    return dialog
