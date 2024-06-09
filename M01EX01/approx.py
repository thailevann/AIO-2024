# Approximations for Sin(x), Cos(x), Sinh(x), Cosh(x)
def factorial(x):
    fac = 1
    for i in range(1, x + 1):
        fac *= i
    return fac

def approx_sin(x, n):
    approx = 0
    for i in range(n):
        term = ((-1)**i) * (x**(2 * i + 1)) / factorial(2 * i + 1)
        approx += term
    return approx

def approx_cos(x, n):
    approx = 0
    for i in range(n):
        term = ((-1)**i) * (x**(2 * i)) / factorial(2 * i)
        approx += term
    return approx

def approx_sinh(x, n):
    approx = 0
    for i in range(n):
        term = (x**(2 * i + 1)) / factorial(2 * i + 1)
        approx += term
    return approx

def approx_cosh(x, n):
    approx = 0
    for i in range(n):
        term = (x**(2 * i)) / factorial(2 * i)
        approx += term
    return approx

def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    x = input("Input x: ")
    n = input("Input n: ")
    
    if represents_int(n):
        n = int(n)
        if n > 0:
            x = float(x)
            print(f'sin(x = {x}) ≈ {approx_sin(x, n)}')
            print(f'cos(x = {x}) ≈ {approx_cos(x, n)}')
            print(f'sinh(x = {x}) ≈ {approx_sinh(x, n)}')
            print(f'cosh(x = {x}) ≈ {approx_cosh(x, n)}')
        else:
            print("n must be greater than zero")
    else:
        print("n must be an integer and greater than zero")
