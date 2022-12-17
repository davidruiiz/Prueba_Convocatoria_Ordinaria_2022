"""
Crea función que calcula el millonésimo número en la recurrencia de Fibonacci, sabiendo que debe usar un algoritmo iterativo para calcular el millonésimo número en la recurrencia de Fibonacci.Para ello ejecute los siguientes pasos
Primero, se inicializan los dos primeros números en la recurrencia (0 y 1).
Luego, se calculan los números sucesivos en la recurrencia usando la fórmula c = a + b, donde c es el número en la posición n, a es el número en la posición n - 1 y b es el número en la posición n - 2.
Este proceso se repite hasta llegar al millonésimo número en la recurrencia, que se devuelve como resultado.
Escriba un algoritmo que pueda manejar n hasta 2000000.
Su algoritmo debe generar la respuesta entera exacta, con total precisión. Además, debe manejar correctamente los números negativos como entrada.
"""

import sys

def fibonacci_iterative(n:int)->int:
    sys.set_int_max_str_digits(2000000)
    if n<0:
        raise ValueError("Cannot have a negative term!")

    if n==0 or n==1:
        return n

    n_1 = 1
    n_2 = 1
    output_n = 1
    for _ in range(n-2):
        output_n = n_1 + n_2
        n_2 = n_1
        n_1 = output_n

    return output_n

if __name__ == "__main__":
    print(fibonacci_iterative(2000000))