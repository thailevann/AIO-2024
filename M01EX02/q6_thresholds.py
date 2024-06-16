def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)  # Append min if i is less than min
        elif i > max:
            result.append(max)  # Append max if i is greater than max
        else:
            result.append(i)    # Append i if it's within the range
    return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max=max, min=min, data=my_list))
