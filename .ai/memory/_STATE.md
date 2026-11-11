# Estado compartido

## Contexto activo
- AI Second Brain — Universal Context Architecture (UCA).
- Repositorio: https://github.com/joer2040/ai-baseline

## Objetivo actual
Definir los estándares base del repositorio y mantener la continuidad entre IAs.

## Completado
- Índice central con perfil y reglas universales.
- Plantilla y protocolo de handoffs.
- Enlaces a ambos documentos desde _INDEX.md.
- Estado compartido creado en .ai/memory/_STATE.md.
- Carpeta .ai/memory/handoffs/ conservada mediante .gitkeep.
- Referencias a ambas ubicaciones incorporadas en _INDEX.md.

- .gitignore creado para contexto privado y variables de entorno.
- Guía de arranque creada en .ai/workflows/startup_protocol.md.
- Guía de arranque enlazada desde _INDEX.md.
- README.md actualizado con la guía de uso aprobada.
- Plantilla de regla temática creada en .ai/rules/_TEMPLATE.md.
- Plantilla enlazada desde _INDEX.md.
- Configuración compartida UCA 1.0 incorporada en .ai/settings.json.
- Convenciones de configuración documentadas en _INDEX.md y README.md.

- Schema creado en .ai/settings.schema.json y documentado en índice y README.
- Configuración actual validada con jsonschema Draft202012Validator;
  13 casos inválidos rechazados en comprobaciones previas a publicar.

## Decisiones aprobadas
- JSON Schema Draft 2020-12 aprobado para configuración UCA 1.0.
- Configuración UCA 1.0: rutas relativas a la raíz y límites aprobados.
- Ajustes locales sin capacidad de cambiar reglas, autorizaciones
  ni límites compartidos.
- Formato de reglas temáticas aprobado: Markdown con etiquetas XML.
- La plantilla de reglas no constituye una regla activa.
- Estado compartido: .ai/memory/_STATE.md.
- Handoffs completados: .ai/memory/handoffs/.
- Estado limitado a 25 000 bytes UTF-8 y 500 líneas.
- Estado y handoffs compartidos entre IAs.
- Organización de proyectos pospuesta por el usuario.
- Auditoría e inventario pospuestos por el usuario.
- Guía de arranque universal aprobada; cada cliente requiere
  un mecanismo compatible para cargar el índice.

## Pendientes
- Definir los módulos restantes con el usuario.
- Mantener pendientes proyectos y auditoría hasta nueva indicación.

## Próximo paso
- Acordar con el usuario qué módulo diseñar a continuación.
- Autorización para implementar el siguiente módulo: pendiente.
- La creación del schema y la actualización del índice, README y estado
  compartido fueron autorizadas por el usuario.
