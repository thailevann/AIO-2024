def reverse_str(x):
    result = ""
    k = len(x)-1
    while k >= 0:
        result += x[k]
        k -= 1
    return result


x = "I can do it"
assert reverse_str(x) == "ti od nac I"
x = "apricot"
print(reverse_str(x))
