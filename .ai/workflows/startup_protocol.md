# Protocolo de arranque universal

## 1. Leer el índice
- Leer _INDEX.md desde el repositorio o la copia de trabajo.
- Si no es accesible, informar la limitación y solicitar
  el archivo antes de continuar con trabajo dependiente de él.
- No afirmar que se cargó contexto que no se pudo leer.

## 2. Identificar la tarea
- Determinar el contexto activo y el objetivo del usuario.
- Leer .ai/memory/_STATE.md.
- Comprobar que el estado corresponde a la tarea solicitada.
- Consultar el handoff pertinente cuando exista.
- Si hay ambigüedad relevante, preguntar al usuario.

## 3. Cargar contexto específico
- Seguir las referencias del índice y del estado.
- Leer únicamente las reglas y documentos necesarios.
- No cargar todas las carpetas de forma indiscriminada.
- No asumir proyectos, rutas ni herramientas sin evidencia.

## 4. Comprobar las capacidades necesarias
- Identificar las herramientas disponibles para la tarea.
- Leer los contratos aplicables antes de utilizarlas.
- No confundir una configuración documentada con una
  conexión operativa o una autorización de ejecución.
- Si falta un contrato necesario, señalarlo antes de
  ejecutar la acción que dependa de él.

## 5. Retomar el trabajo
- Comparar el estado y el handoff con los archivos actuales.
- Resolver contradicciones relevantes antes de editar.
- Continuar dentro del alcance autorizado.
- Aplicar el protocolo de handoffs al cerrar la tarea.

## Integración con clientes
Este documento describe el comportamiento esperado.
Cada cliente necesita un mecanismo compatible para dirigir
a la IA hacia _INDEX.md.

La existencia de estos archivos no garantiza su carga
automática ni habilita herramientas o permisos.
