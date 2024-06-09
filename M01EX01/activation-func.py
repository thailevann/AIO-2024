# Calculate sigmoid function, ReLU function, and ELU function
import math

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def sigmoid_func(x):
    x = float(x)
    return 1 / (1 + math.exp(-x))

def relu_func(x):
    x = float(x)
    return max(0, x)

def elu_func(x, alpha=0.01):
    x = float(x)
    return x if x > 0 else alpha * (math.exp(x) - 1)

if __name__ == "__main__":
    x = input("Input x: ")
    if is_number(x):
        func_name = input("Input activation function (sigmoid | relu | elu): ").strip().lower()
        if func_name == 'sigmoid':
            output = sigmoid_func(x)
        elif func_name == 'relu':
            output = relu_func(x)
        elif func_name == 'elu':
            output = elu_func(x)
        else:
            print(f'{func_name} is not supported')
            exit()
        print(f'{func_name}: f({x}) = {output}')
    else:
        print('x must be a number')
