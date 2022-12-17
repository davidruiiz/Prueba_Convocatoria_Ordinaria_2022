"""
Cree una función expand que tome una expresión con una sola variable de una letra y la expanda. La fórmula tiene la forma (ax b)^n. donde a y b son números enteros positivos o negativos, x es cualquier variable de un solo carácter y n es un número natural.
Si a = 1, no se antepone ningún coeficiente a la variable.
Si a = -1, la variable tiene el prefijo "-".
La forma expandida debe devolverse como una cadena de la forma ax^b cx^d ex^f... donde a, c y e son los coeficientes del término y x es la variable original de una letra pasada.
La fórmula original y b, d y f son potencias de x en cada término, en orden descendente. Si el coeficiente de un término es cero, ese término no debe incluirse. Si un término tiene un coeficiente de 1, no incluya ese coeficiente.
Si un término tiene un coeficiente de -1, debe contener solo "-".
Si el término tiene una potencia de 0, solo se debe incluir el coeficiente. Si el término tiene una potencia de 1, el signo de intercalación y la potencia deben excluirse.
"""