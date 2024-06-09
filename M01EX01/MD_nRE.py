# Calculate Mean Difference of nth Root Error
def md_nre(y_true, y_predict, n, p):
    return (y_true ** (1 / n) - y_predict ** (1 / n)) ** p

if __name__ == "__main__":
    n = float(input("Input n: "))
    p = float(input("Input p: "))
    y_predict = float(input("Input y_predict: "))
    y_true = float(input("Input y_true: "))
    
    result = md_nre(y_true, y_predict, n, p)
    print(result)
