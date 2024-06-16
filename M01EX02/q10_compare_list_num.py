def my_function(integers, number=1):
    result = []
    for i in integers:
        if i == number:
            result.append(True)
        else:
            result.append(False)
    if True in result:
        return True
    else:
        return False


my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))
