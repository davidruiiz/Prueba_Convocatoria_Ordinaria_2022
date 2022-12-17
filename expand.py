"""
Cree una función expand que tome una expresión con una sola variable de una letra y la expanda. La fórmula tiene la forma (ax b)^n. donde a y b son números enteros positivos o negativos, x es cualquier variable de un solo carácter y n es un número natural.
Si a = 1, no se antepone ningún coeficiente a la variable.
Si a = -1, la variable tiene el prefijo "-".
La forma expandida debe devolverse como una cadena de la forma ax^b cx^d ex^f... donde a, c y e son los coeficientes del término y x es la variable original de una letra pasada.
La fórmula original y b, d y f son potencias de x en cada término, en orden descendente. Si el coeficiente de un término es cero, ese término no debe incluirse. Si un término tiene un coeficiente de 1, no incluya ese coeficiente.
Si un término tiene un coeficiente de -1, debe contener solo "-".
Si el término tiene una potencia de 0, solo se debe incluir el coeficiente. Si el término tiene una potencia de 1, el signo de intercalación y la potencia deben excluirse.
"""

import re
from typing import List, Tuple

def expand(formula:str)->str:
    """
    Expands a formula of the form (ax+b)^n, where a and b are integers, x is a variable and n is a natural number.
    """
    # Check if the formula is valid
    if not re.match(r"\([a-zA-Z]\d*[+-]\d*\)\^\d+", formula):
        raise ValueError("Invalid formula!")

    # Get the variable
    variable = re.search(r"[a-zA-Z]", formula).group(0)

    # Get the coefficients
    coefficients = re.findall(r"[-+]?\d+", formula)

    # Get the exponent
    exponent = int(re.search(r"\^\d+", formula).group(0)[1:])

    # Get the expanded formula
    expanded_formula = expand_formula(variable, coefficients, exponent)

    return expanded_formula

def expand_formula(variable:str, coefficients:List[str], exponent:int)->str:
    """
    Expands a formula of the form (ax+b)^n, where a and b are integers, x is a variable and n is a natural number.
    """
    # Get the coefficients
    a = int(coefficients[0])
    b = int(coefficients[1])

    # Get the expanded formula
    expanded_formula = expand_formula_iterative(variable, a, b, exponent)

    return expanded_formula

def expand_formula_iterative(variable:str, a:int, b:int, exponent:int)->str:
    """
    Expands a formula of the form (ax+b)^n, where a and b are integers, x is a variable and n is a natural number.
    """
    # Get the expanded formula
    expanded_formula = ""
    for i in range(exponent+1):
        # Get the coefficient
        coefficient = get_coefficient(a, b, exponent, i)

        # Get the power
        power = get_power(exponent, i)

        # Get the term
        term = get_term(variable, coefficient, power)

        # Add the term to the expanded formula
        expanded_formula += term

    return expanded_formula

def get_coefficient(a:int, b:int, exponent:int, i:int)->int:
    """
    Gets the coefficient of a term in the expansion of a formula of the form (ax+b)^n, where a and b are integers, x is a variable and n is a natural number.
    """
    # Get the coefficient
    coefficient = int(combination(exponent, i) * a**(exponent-i) * b**i)

    return coefficient

def get_power(exponent:int, i:int)->int:
    """
    Gets the power of a term in the expansion of a formula of the form (ax+b)^n, where a and b are integers, x is a variable and n is a natural number.
    """
    # Get the power
    power = exponent - i

    return power

def get_term(variable:str, coefficient:int, power:int)->str:
    """
    Gets a term in the expansion of a formula of the form (ax+b)^n, where a and b are integers, x is a variable and n is a natural number.
    """
    # Get the term
    if coefficient == 0:
        term = ""
    elif coefficient == 1:
        if power == 0:
            term = "1"
        elif power == 1:
            term = variable
        else:
            term = f"{variable}^{power}"
    elif coefficient == -1:
        if power == 0:
            term = "-1"
        elif power == 1:
            term = f"-{variable}"
        else:
            term = f"-{variable}^{power}"
    else:
        if power == 0:
            term = str(coefficient)
        elif power == 1:
            term = f"{coefficient}{variable}"
        else:
            term = f"{coefficient}{variable}^{power}"

    return term

def combination(n:int, k:int)->int:
    """
    Gets the combination of n and k.
    """
    # Get the combination
    combination = factorial(n) / (factorial(k) * factorial(n-k))

    return combination

def factorial(n:int)->int:
    """
    Gets the factorial of n.
    """
    # Get the factorial
    if n == 0:
        factorial = 1
    else:
        factorial = n * factorial(n-1)

    return factorial

if __name__ == "__main__":
    # Get the formula
    formula = input("Enter the formula: ")

    # Expand the formula
    expanded_formula = expand(formula)

    # Print the expanded formula
    print(expanded_formula)

"""
Enter the formula: (x+1)^2
x^2+2x+1
"""
