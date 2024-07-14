import pandas as pd
import numpy as np
df = pd.read_csv("./csv_data/advertising.csv")
data = df.to_numpy()

#Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales:
def get_max_index(data):
    return np.max(data[:,3]),  np.argmax(data[:, 3])
#16: Giá trị trung bình của cột TV 
def get_mean_index(data):
    return np.mean(data[:,0]),  np.argmax(data[:, 0])

#question 15
max_data, index = get_max_index(data)
print(f'max: {max_data} , index: {index}')

#question 16
mean_data, index = get_mean_index(data)
print(f'mean: {mean_data} , index: {index}')

#question 17
get_element_larger_20= np.sum(data[:,3]>=20)
print(f'{get_element_larger_20}')

#question 18
get_element_larger_15 = data[data[:,3] >= 15]
average_radio = np.mean(get_element_larger_15[:, 1])

print(f'{average_radio}')

#question 19
filtered= data[data[:,2] >= np.mean(data[:,2])]
result = np.sum(filtered[:, 3])
print(f'{result}')

#question 20
mean_sales = np.mean(data[:,3])
scores = np.empty_like(data[:,3], dtype=str)
scores[data[:,3] > mean_sales] = 'Good'
scores[data[:,3]< mean_sales] = 'Bad'
scores[data[:,3] == mean_sales] = 'Average'
print("Các giá trị trong mảng scores từ vị trí 7 đến vị trí 9 là:", scores[7:10])

#question 21
# Tìm giá trị trong cột Sales gần nhất với giá trị trung bình A
nearest_value_to_mean_sales= data[:,3][np.abs(data[:,3] - mean_sales).argmin()]

scores = np.empty_like(data[:,3], dtype=str)
scores[data[:,3] > nearest_value_to_mean_sales] = 'Good'
scores[data[:,3]< nearest_value_to_mean_sales] = 'Bad'
scores[data[:,3] ==nearest_value_to_mean_sales] = 'Average'
print("Các giá trị trong mảng scores từ vị trí 7 đến vị trí 9 là:", scores[7:10])

