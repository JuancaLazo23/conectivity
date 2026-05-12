# Integracion minima: Sediment Connectivity Bridge Test

## Que es este entregable

Este entregable es una prueba tecnica minima tipo bridge/smoke test para validar que QSWATPlus IGP puede importar e invocar un modulo externo de conectividad sedimentaria.

Ruta del entregable:

`C:\IGP\versiones_laptop\ref_princip_laptop\connectivity_bridge_test`

## Que NO es este entregable

No es el modulo cientifico completo. No contiene runner final, rutinas largas de MUSLE, FCI, DSC, calibracion, eventos, procesamiento raster, DEM, HRUs, `usersoil.csv` ni datos de Ronquillo. Tampoco modifica automaticamente el plugin principal QSWATPlus.

## Que prueba permite hacer

Permite verificar que desde QSWATPlus IGP se pueda:

- disponer de un boton temporal,
- agregar la carpeta del bridge al `sys.path`,
- importar `connectivity_bridge.public_api`,
- ejecutar `test_import()`,
- abrir una ventana minima con `open_connectivity_dialog(...)`.

## API publica disponible

El modulo `connectivity_bridge.public_api` expone:

- `get_module_info()`
- `test_import()`
- `open_connectivity_dialog(iface=None, parent=None, project_context=None)`

## Prueba standalone

Desde PowerShell o consola Python, ejecutar:

```powershell
cd C:\IGP\versiones_laptop\ref_princip_laptop\connectivity_bridge_test
python tests\test_import_standalone.py
```

Resultado esperado:

- se agrega temporalmente la carpeta raiz al `sys.path`,
- se importa `connectivity_bridge.public_api`,
- `get_module_info()` devuelve metadatos,
- `test_import()` devuelve `ok=True`.

## Prueba desde consola Python de QGIS

Abrir QGIS, abrir la consola Python y ejecutar o pegar:

```python
exec(open(r"C:\IGP\versiones_laptop\ref_princip_laptop\connectivity_bridge_test\tests\qgis_console_smoke_test.py", encoding="utf-8").read())
```

Resultado esperado:

- la consola muestra `test_import()` con `ok=True`,
- se abre una ventana minima titulada "Módulo de Conectividad Sedimentaria",
- la ventana indica que el bridge fue cargado correctamente desde QSWATPlus IGP.

## Integracion temporal como boton en QSWATPlus IGP

No se aplica ningun cambio automatico al plugin principal. Para integrar temporalmente un boton, revisar:

`integration_snippets\qswatplus_button_snippet.py`

El punto recomendado identificado durante la inspeccion es:

`C:\IGP\versiones_laptop\ref_princip_laptop\QSWATPlus\QSWATPlusMain.py`

Dentro de la clase `QSWATPlus`, el registro de acciones se realiza en `initGui()` y la limpieza en `unload()`. Tambien existe un placeholder de conectividad en `open_event_dsc_dialog()`, que puede servir como referencia.

## Resultado esperado para el compañero integrador

Al hacer clic en el boton "Probar modulo de conectividad sedimentaria", QSWATPlus IGP debe poder importar el paquete `connectivity_bridge`, ejecutar `test_import()` y abrir una ventana minima indicando que el modulo fue cargado correctamente. Esta prueba no ejecuta el runner cientifico ni procesa datos; solo valida el acoplamiento tecnico.

## Pasos siguientes si la prueba funciona

Si el bridge se invoca correctamente desde QSWATPlus IGP, el siguiente paso es acordar una API estable para el modulo real, por ejemplo:

- entrada de contexto de proyecto QSWATPlus,
- validacion de rutas del proyecto,
- diagnosticos de disponibilidad de datos,
- punto de entrada del runner cientifico,
- manejo de mensajes y errores hacia la interfaz QGIS.
