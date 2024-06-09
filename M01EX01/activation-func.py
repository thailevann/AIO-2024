#caculate sigmoid function, relu function and elu function
import math
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def c(x):
    x = float(x)
    return 1/(1+math.e**(-x))

def relu_func(x):
    x = float(x)
    if x <= 0:
        return 0
    else:
        return x

def elu_func(x, alpha = 0.01):
    x = float(x)
    if x <= 0:
        return alpha*(math.e**x-1)
    else:
        return x
def sigmoid_func(x):
     return 1/(1+math.e**(-x))

if __name__== "__main__":
    print("Input x = ")
    x = input()
    if is_number(x) == True:
        print("Input activation Function (sigmoid|relu|elu):")
        func_name = input()
        if func_name == 'sigmoid':
            output = sigmoid_func(x)
            print(f'{func_name}: f({x}) = {output} ')
        elif func_name == 'relu':
            output = relu_func(x)
            print(f'{func_name}: f({x}) = {output} ')
        elif func_name == "elu":
            output = elu_func(x)
            print(f'{func_name}: f({x}) = {output} ')
        else:
            print(f'{func_name} is not supported')
    else:
        print('x must be a number')

