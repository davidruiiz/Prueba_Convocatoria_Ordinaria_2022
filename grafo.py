"""
En un patrón, los puntos/puntos no se pueden repetir: solo se pueden usar una vez, como máximo.
En un patrón, dos puntos/puntos posteriores cualesquiera solo se pueden conectar con líneas rectas directas de cualquiera de estas formas:
Horizontalmente: como (A -> B) en la imagen del patrón de ejemplo.
Verticalmente: como (D -> G) en la imagen del patrón de ejemplo.
En diagonal: como (I -> E), así como (B -> I), en la imagen del patrón de ejemplo.
Pasando por encima de un punto entre ellos que ya ha sido 'usado': como (G -> C) pasando por encima de E, en la imagen del patrón de ejemplo. Esta es la regla más complicada. Normalmente, no podría conectar G con C, porque E está entre ellos, sin embargo , cuando E ya se ha utilizado como parte del patrón que está rastreando, puede conectar G con C pasando por E , porque E se ignora , como ya se usó una vez.
"""

