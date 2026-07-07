# Propuesta de Proyecto: Simulador Interactivo de Filogenia (UPGMA)

## 1. Objetivo del simulador

Este simulador busca enseñar cómo se construye un árbol evolutivo a partir de la comparación genética entre especies o secuencias. La idea es que el estudiante entienda el proceso de agrupamiento paso a paso, sin perderse en cálculos matemáticos avanzados, viendo en tiempo real cómo las distancias genéticas se transforman en relaciones de parentesco.

El algoritmo base elegido es **UPGMA** (Unweighted Pair Group Method with Arithmetic mean), un método clásico y ampliamente usado para construir árboles filogenéticos a partir de una matriz de distancias.

## 2. Público objetivo

Estudiantes de nivel introductorio en biología o bioinformática, por ejemplo primeros semestres de pregrado, que ya conocen el concepto de ADN y mutación, pero que aún no han trabajado con árboles filogenéticos ni con algoritmos de agrupamiento.

## 3. Justificación biológica

La filogenia estudia las relaciones evolutivas entre organismos, y una de las formas más comunes de representarla es a través de árboles construidos a partir de distancias genéticas. La lógica detrás es simple: dos especies que comparten un ancestro común reciente tienden a tener secuencias de ADN o proteínas más parecidas entre sí, mientras que especies que se separaron hace mucho tiempo acumulan más diferencias.

UPGMA parte de esta idea. Toma una matriz de distancias, es decir una tabla que indica qué tan diferentes son las secuencias entre cada par de especies, y en cada paso agrupa a las dos especies o grupos más cercanos. Luego recalcula las distancias del nuevo grupo hacia el resto usando un promedio, y repite el proceso hasta que todo queda unido en un solo árbol.

Vale la pena aclarar en el simulador que UPGMA asume que todas las ramas evolucionan a la misma velocidad, lo cual es una simplificación. En la vida real esto no siempre se cumple, y por eso existen otros métodos como Neighbor-Joining que no hacen esa suposición. Para efectos educativos, esta simplificación es aceptable porque permite construir un árbol de forma más directa y visual.

## 4. Simplificaciones para el usuario

Para que el simulador sea accesible a estudiantes que recién están aprendiendo el tema, se van a aplicar las siguientes simplificaciones:

- El usuario ingresa una matriz de distancias pequeña (entre 4 y 6 especies), en vez de secuencias genómicas completas.
- No se trabaja con secuencias de ADN reales dentro del simulador, sino con valores numéricos que representan distancias ya calculadas, para enfocarse en el algoritmo de agrupamiento y no en el cálculo de distancias en sí.
- Se muestra cada paso del agrupamiento de forma visual y explicada, en vez de solo mostrar el resultado final.
- El árbol final se dibuja de forma simple, sin escalas de tiempo evolutivo reales, priorizando que se entienda el orden de agrupamiento.

## 5. Flujo lógico del simulador

1. El usuario ingresa el número de especies y sus nombres.
2. El usuario ingresa la matriz de distancias entre cada par de especies (o el simulador ofrece una matriz de ejemplo para quien no tenga datos propios).
3. El sistema identifica el par con la distancia más pequeña.
4. Ese par se une en un nuevo grupo, y se muestra visualmente esta unión en el árbol.
5. El sistema recalcula las distancias del nuevo grupo hacia las especies o grupos restantes, usando el promedio.
6. Se repiten los pasos 3 a 5 hasta que solo queda un grupo, formando el árbol completo.
7. El usuario puede ver el árbol final y revisar el orden en que se hicieron las agrupaciones.
8. Se ofrece un modo de autoevaluación donde el estudiante debe predecir cuál par se va a agrupar primero, antes de que el sistema lo revele.

## 6. Herramientas y tecnología

- **Lenguaje:** Python
- **Interfaz:** Streamlit, para desplegar el simulador como página web de forma sencilla
- **Visualización del árbol:** Matplotlib o una librería de árboles filogenéticos compatible con Python
- **Despliegue final:** Streamlit Community Cloud

## 7. Validación

Los resultados del simulador se van a comparar con herramientas reales de filogenia, como las disponibles en NCBI o software de referencia como MEGA, usando los mismos datos de entrada, para confirmar que el árbol generado coincide en su lógica de agrupamiento.
