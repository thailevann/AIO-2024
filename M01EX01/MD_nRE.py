# Calculate Mean Difference of nth Root Error
def MD_nRE(y_true, y_predict, n, p):
    return (y_true**(1/n) - y_predict**(1/n))**p

if __name__ == "__main__":
    n = float(input("Input n: "))
    p = float(input("Input p: "))
    y_predict = float(input("Input y predict: "))
    y_true = float(input("Input y true: "))
    
    result = MD_nRE(y_true, y_predict, n, p)
    print(result)
