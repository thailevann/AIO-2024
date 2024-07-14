import numpy as np
#create a 1d array from 0 to 9
arr = np.arange(0,10,1)
print(f"a 1d array 1d from 0 to 9: {arr}")

# Create a 3x3 boolean array with all values set to True
arr = np.ones((3,3))>0
print(f"a 3x3 boolean array with all values set to True \n {arr}")
arr = np.ones((3,3), dtype = bool)
print(f"a 3x3 boolean array with all values set to True \n {arr}")
arr = np.full((3,3), fill_value = True, dtype = bool)
print(f"a 3x3 boolean array with all values set to True \n {arr}")

#question 3
arr = np.arange(0,10)
print(arr[arr%2 == 1])

#question 4
arr = np.arange(0,10)
arr[arr%2==1] = -1
print(arr)

#question 5
arr = np.arange(10)
arr_2d = arr.reshape(2,-1) #mảng 2 hàng, -1 giúp số cột sẽ được tính toán tự động 
print(arr_2d)

#question 6
arr1 = np.arange(10).reshape(2,-1)
arr2 = np.repeat(1,10).reshape(2,-1) # lặp lại phần tử 1 mười lần.
c = np.concatenate([arr1, arr2], axis = 0)
print(c)

#question 7
arr1 = np.arange(10).reshape(2,-1)
arr2 = np.repeat(1,10).reshape(2,-1) # lặp lại phần tử 1 mười lần.
c = np.concatenate([arr1, arr2], axis = 1)
print(c)

#question 8
arr = np.array([1,2,3])
print(np.repeat(arr,3)) #[1 1 1 2 2 2 3 3 3]
print(np.tile(arr,3)) #[1 2 3 1 2 3 1 2 3]

#question 9
a = np.array([2,6,1,9,10,3,27])
index = np.where((a >= 5) & (a <= 10))
print(a[index])

#question 10
def maxx(x,y):
    if x >= y:
        return x
    else:
        return y
a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])
#numpy.vectorize(pyfunc, otypes=None, doc=None, excluded=None, cache=False, signature=None)
#áp dụng hàm maxx cho từng cặp phần tử tương ứng từ arr1 và arr2, và kết quả sẽ là một mảng mới chứa các giá trị lớn hơn từ mỗi cặp, với kiểu dữ liệu là float.
pair_max = np.vectorize(maxx, otypes = [float])
print(pair_max)

#question 11
a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])

print(np.where(a<b, b,a))

