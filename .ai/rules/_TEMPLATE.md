# Plantilla de regla temática

Esta plantilla no es una regla activa.
Los campos entre corchetes deben completarse antes de usarla.

<rule id="[identificador]" version="1.0">

<status>
[borrador | aprobada | retirada]
</status>

<scope>
[Tema y situaciones donde aplica.]
</scope>

<load_when>
[Condiciones concretas para consultar esta regla.]
</load_when>

<directives>
- [Instrucción concreta y verificable.]
- [Instrucción concreta y verificable.]
</directives>

<conflicts>
- Aplicar esta regla únicamente dentro de su alcance
  y cuando su estado sea "aprobada".
- Respetar las instrucciones de mayor prioridad y los
  permisos del entorno.
- No interpretar esta regla como autorización adicional.
- Si existe una contradicción sin resolver, señalarla
  y solicitar la decisión necesaria antes de actuar
  sobre el punto afectado.
</conflicts>

</rule>
