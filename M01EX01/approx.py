#Approximations for Sin(x), Cos(x), Sinh(x), Cosh(x)
def factorial(x):
    fac = 1
    if x  == 0 or x == 1:
        return 1
    for i in range(1, x+1):
        fac = fac * i
    return fac

def approx_sin(x, n):
    approx = 0
    for i in range(0,n):
        s1 = (-1)**i
        s2 = x**(2*i+1)
        s3 = factorial(2*i+1)
        s = s1*s2/s3
        approx = approx + s
    return approx
def approx_cos(x,n):
    approx = 0
    for i in range(0,n):
        s1 = (-1)**i
        s2 = x**(2*i)
        s3 = factorial(2*i)
        s = s1*s2/s3
        approx = approx + s
    return approx

def approx_sinh(x,n):
    approx = 0
    for i in range(0,n):
        s2 = x**(2*i+1)
        s3 = factorial(2*i+1)
        s = s2/s3
        approx = approx + s
    return approx

def approx_cosh(x,n):
    approx = 0
    for i in range(0,n):
        s2 = x**(2*i)
        s3 = factorial(2*i)
        s = s2/s3
        approx = approx + s
    return approx
def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True
if __name__== "__main__":

    print("Input x = ")
    x = input()
    print("Input n = ")
    n = input()
    if represents_int(n) == True:
        if n <= 0:
            x = float(x)
            n = int(n)
            print(f'sin(x = {x}) = {approx_sin(x,n)}')
            print(f'cos(x = {x}) = {approx_cos(x,n)}')
            print(f'sinh(x = {x}) = {approx_sinh(x,n)}')
            print(f'cosh(x = {x}) = {approx_cosh(x,n)}')
    else:
        print("n must be int and greater than zero")

