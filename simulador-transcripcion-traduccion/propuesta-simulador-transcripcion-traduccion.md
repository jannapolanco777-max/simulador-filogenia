# Propuesta de Proyecto: Visualizador Interactivo de Transcripción y Traducción del ADN

## 1. Objetivo del simulador

Este simulador busca enseñar, de forma visual y paso a paso, cómo la información genética contenida en el ADN se convierte en una proteína funcional. El proceso completo tiene dos etapas: la transcripción, donde el ADN se copia a ARN mensajero, y la traducción, donde ese ARN mensajero se lee para construir una cadena de aminoácidos.

El simulador permite al usuario ingresar una secuencia corta de ADN y observar en tiempo real cómo se transforma primero en ARN y después en una proteína, letra por letra y codón por codón.

## 2. Público objetivo

Estudiantes de nivel introductorio en biología o bioinformática, que ya conocen los conceptos básicos de ADN, ARN y proteínas, pero que aún no han trabajado de forma práctica con el proceso de expresión génica.

## 3. Justificación científica

La expresión génica es el proceso mediante el cual la información almacenada en el ADN se utiliza para producir proteínas, las moléculas que realizan la mayoría de las funciones dentro de una célula. Este flujo de información, que va del ADN al ARN y del ARN a la proteína, fue formulado originalmente por Francis Crick como el dogma central de la biología molecular (Crick, 1970). Este proceso ocurre en dos grandes pasos.

En la transcripción, una enzima llamada ARN polimerasa recorre una hebra de ADN y construye una molécula complementaria de ARN mensajero. La diferencia principal entre ambas moléculas es que el ARN usa la base Uracilo (U) en lugar de la Timina (T) que usa el ADN. El resto de las bases (Adenina, Citosina y Guanina) se mantienen igual.

En la traducción, el ARN mensajero es leído por el ribosoma en grupos de tres bases llamados codones. Cada codón corresponde a un aminoácido específico, según una tabla fija conocida como el código genético. La existencia de este código de tripletes fue demostrada experimentalmente por primera vez por Nirenberg y Matthaei (1961), quienes identificaron que la secuencia de ARN compuesta solo por uracilo codificaba el aminoácido fenilalanina, marcando el inicio del descifre completo del código genético.

Enseñar este proceso de forma interactiva ayuda al estudiante a comprender que una proteína no aparece de la nada, sino que es el resultado directo y mecánico de leer una secuencia de ADN siguiendo reglas fijas y conocidas. El uso de simulaciones computacionales para enseñar procesos moleculares como este ha demostrado ser una alternativa efectiva a las prácticas de laboratorio tradicionales, mejorando la comprensión de estudiantes universitarios sobre estructuras y procesos de ácidos nucleicos (Fu et al., 2025).

## 4. Simplificaciones para el usuario

- El usuario trabaja con secuencias de ADN cortas (entre 15 y 30 bases), en lugar de genes completos, para que el proceso sea fácil de seguir visualmente.
- No se simulan errores de transcripción ni mutaciones en esta primera versión, solo el proceso ideal y correcto.
- Se asume que la secuencia ingresada ya representa la hebra molde lista para transcribir, sin entrar en detalles de promotores ni regiones regulatorias.
- El código genético se simplifica a los codones más comunes, mostrando el nombre del aminoácido de forma clara junto a su abreviatura.

## 5. Flujo lógico del simulador

1. El usuario ingresa una secuencia de ADN (o usa un ejemplo precargado).
2. El sistema valida que la secuencia solo contenga las letras A, T, C y G.
3. El simulador transcribe la secuencia a ARN mensajero, mostrando el cambio de cada base T por U, letra por letra.
4. El simulador divide el ARN mensajero en codones, agrupando de tres en tres bases.
5. Cada codón se traduce a su aminoácido correspondiente, mostrando el resultado paso a paso.
6. Se arma visualmente la cadena de aminoácidos final, representando la proteína resultante.
7. El usuario puede ver el resumen completo: ADN original, ARN transcrito, y la secuencia de aminoácidos.
8. Se ofrece un modo de autoevaluación donde el estudiante debe predecir a qué aminoácido corresponde un codón específico, antes de que el sistema lo revele.

## 6. Herramientas y tecnología

- **Lenguaje:** Python
- **Interfaz:** Streamlit, un framework que ha facilitado la creación de aplicaciones web para bioinformática sin necesidad de conocimientos de desarrollo web tradicional (Nantasenamat et al., 2023).
- **Validación:** comparación de resultados contra Biopython (Cock et al., 2009), específicamente su módulo Bio.Seq, que incluye funciones de transcripción y traducción ya probadas y usadas en investigación real.
- **Despliegue final:** Streamlit Community Cloud

## 7. Validación

Los resultados del simulador se van a comparar con las funciones `transcribe()` y `translate()` del módulo Bio.Seq de Biopython, usando la misma secuencia de ADN de entrada, para confirmar que el ARN generado y la proteína resultante coinciden exactamente con los de una herramienta profesional real.

## 8. Referencias

### Fuentes recientes (últimos 5 años)

Fu, J., Monte Carlo, A., & Zheng, D. (2025). Incorporation of NUPACK-based simulation into classroom and laboratory teaching of nucleic acids hybridization for undergraduate biochemistry. *Journal of Chemical Education*. https://doi.org/10.1021/acs.jchemed.4c01051

Nantasenamat, C., Biswas, A., Nápoles-Duarte, J. M., Parker, M. I., & Dunbrack, R. L. Jr. (2023). Building bioinformatics web applications with Streamlit. En *Cheminformatics, QSAR and Machine Learning Applications for Novel Drug Development* (pp. 559-571). Academic Press.

### Fuentes originales del proceso biológico y las herramientas

Estas son las publicaciones donde se describieron por primera vez el dogma central de la biología molecular, el código genético, y la herramienta de validación. Se citan por convención académica, ya que son la fuente primaria de estos conceptos y métodos, sin importar su antigüedad.

Crick, F. (1970). Central dogma of molecular biology. *Nature*, 227(5258), 561-563. https://doi.org/10.1038/227561a0

Nirenberg, M. W., & Matthaei, J. H. (1961). The dependence of cell-free protein synthesis in E. coli upon naturally occurring or synthetic polyribonucleotides. *Proceedings of the National Academy of Sciences*, 47(10), 1588-1602. https://doi.org/10.1073/pnas.47.10.1588

Cock, P. J. A., Antao, T., Chang, J. T., Chapman, B. A., Cox, C. J., Dalke, A., Friedberg, I., Hamelryck, T., Kauff, F., Wilczynski, B., & de Hoon, M. J. L. (2009). Biopython: Freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics*, 25(11), 1422-1423. https://doi.org/10.1093/bioinformatics/btp163
