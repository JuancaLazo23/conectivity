# Instrucciones para integrador QSWATPlus IGP

## Hallazgos de inspeccion no invasiva

Repositorio inspeccionado:

`C:\IGP\versiones_laptop\ref_princip_laptop\QSWATPlus`

Punto principal del plugin:

`C:\IGP\versiones_laptop\ref_princip_laptop\QSWATPlus\QSWATPlusMain.py`

La clase principal identificada es `QSWATPlus`. El registro de acciones/botones se hace en `initGui()`:

- `QAction(...)`
- `self._iface.addToolBarIcon(...)`
- `self._iface.addPluginToMenu(...)`

La limpieza de acciones se hace en `unload()`:

- `self._iface.removePluginMenu(...)`
- `self._iface.removeToolBarIcon(...)`

Tambien existe un placeholder ya integrado para conectividad:

- atributo `self._event_dsc_action`
- metodo `open_event_dsc_dialog()`
- carpeta existente `connectivity\`

## Punto logico recomendado

Para una prueba temporal, el punto mas simple es copiar/adaptar el contenido de:

`integration_snippets\qswatplus_button_snippet.py`

dentro de `QSWATPlusMain.py`, en la clase `QSWATPlus`:

1. Llamar `add_connectivity_bridge_action(self)` al final de `initGui()`.
2. Llamar `remove_connectivity_bridge_action(self)` dentro de `unload()`.
3. Ajustar el texto del menu si el plugin IGP usa un nombre distinto de `&QSWAT+`.

## Alternativa si se quiere reutilizar el placeholder existente

El metodo `open_event_dsc_dialog()` ya funciona como patron para abrir una ventana del modulo actual. El integrador puede cambiar temporalmente su implementacion para que llame:

```python
from connectivity_bridge.public_api import open_connectivity_dialog, test_import

test_import()
open_connectivity_dialog(iface=self._iface, parent=self._iface.mainWindow())
```

Antes de importar, debe agregarse al `sys.path`:

```python
bridge_root = r"C:\IGP\versiones_laptop\ref_princip_laptop\connectivity_bridge_test"
if bridge_root not in sys.path:
    sys.path.insert(0, bridge_root)
```

## Importante

Este bridge no ejecuta calculos cientificos. Solo valida que QSWATPlus IGP pueda:

- encontrar el paquete externo,
- importar la API publica,
- responder a `test_import()`,
- abrir una ventana minima desde QGIS.

