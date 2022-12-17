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