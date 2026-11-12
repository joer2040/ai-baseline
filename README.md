# AI Second Brain — UCA

Repositorio central de contexto para colaborar con distintas
IAs mediante una base compartida, explícita y versionada.

UCA es la convención de organización adoptada en este repositorio.
Cada aplicación requiere una integración compatible para utilizarla.

## Punto de entrada

Las IAs deben comenzar leyendo [_INDEX.md](_INDEX.md).
Este archivo contiene el perfil base, las reglas de colaboración
y las referencias necesarias para continuar.

## Organización

| Ruta | Contenido |
|---|---|
| _INDEX.md | Perfil, reglas y mapa del contexto. |
| CLAUDE.md | Redirección al índice para clientes compatibles. |
| .ai/settings.json | Rutas y límites compartidos en formato UCA 1.0. |
| .ai/rules/ | Ubicación reservada para reglas específicas. |
| .ai/skills/ | Ubicación reservada para skills y contratos. |
| .ai/workflows/ | Protocolos y plantillas de trabajo. |
| .ai/memory/_STATE.md | Estado vigente compartido entre IAs. |
| .ai/memory/handoffs/ | Relevos completados entre sesiones. |

## Iniciar una sesión

Proporciona a la IA acceso al repositorio e indica:

> Lee _INDEX.md de joer2040/ai-baseline. Sigue el protocolo
> de arranque y consulta el estado compartido antes de continuar.
> Si no puedes acceder a algún archivo necesario, indícalo.

El protocolo está en:
[Arranque universal](.ai/workflows/startup_protocol.md).

La carga automática depende de la configuración de cada cliente.
Guardar archivos en GitHub no configura las aplicaciones.

## Cerrar o transferir una tarea

Usar el [protocolo de handoffs](.ai/workflows/handoff_protocol.md)
y la [plantilla de relevo](.ai/workflows/handoff_template.md).

Actualizar el estado compartido dentro del alcance autorizado.
El estado conserva la situación vigente y los handoffs registran
los relevos. Si no se puede guardar, entregar el relevo en el chat
e indicar que su persistencia queda pendiente.

Cada _STATE.md tiene un máximo de 25 000 bytes UTF-8
y 500 líneas.

## Configuración compartida

[.ai/settings.json](.ai/settings.json) contiene las rutas del contexto
y los workflows, además de los límites del estado compartido.
Todas las rutas se resuelven desde la raíz del repositorio.
Las convenciones están documentadas en [_INDEX.md](_INDEX.md).

Cada integración debe interpretar este formato propio de UCA.
El JSON no aplica configuraciones automáticamente.

### Validación de configuración

Validar .ai/settings.json con [.ai/settings.schema.json](.ai/settings.schema.json)
mediante un validador compatible con JSON Schema Draft 2020-12.
El schema comprueba campos, tipos, versión, formato de rutas y límites
configurados. No comprueba que los destinos existan ni el tamaño real
del estado. Su incorporación no instala ni activa un validador automático.

### Comprobación local del repositorio

Requiere Python 3.10 o posterior. Desde la raíz del repositorio:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_uca.py
```

El script localiza la raíz desde su propia ubicación; no depende del
directorio desde el que se ejecute. Solo lee archivos y reporta errores.
Comprueba el JSON contra su schema, los destinos como archivos o carpetas
y que las rutas resueltas permanezcan dentro del repositorio.
Comprueba también que memory.state sea UTF-8 y no supere sus límites.

Los bytes se cuentan sobre el archivo guardado, incluidos los saltos
de línea. Para contar líneas, LF, CRLF y CR cuentan como un salto;
el salto final no añade una línea vacía y un archivo vacío tiene 0 líneas.

Devuelve 0 cuando todo cumple y 1 ante errores, incluidos JSON inválido,
archivos inaccesibles o una dependencia ausente. La ejecución en
GitHub Actions queda pendiente.

## Configuración privada

.gitignore excluye el contexto y la configuración locales
acordados, además de archivos de variables de entorno.

No guardar credenciales ni secretos en archivos versionados.
Los archivos locales no se cargan automáticamente por existir.

## Pendientes

- Organización y registro de proyectos.
- Auditoría de capacidades por entorno.
- Incorporación de skills, plugins, servidores MCP y conectores.
- Configuración de entrada para cada aplicación.

