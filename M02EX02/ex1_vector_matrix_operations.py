import numpy as np
def compute_vector_length(vector):
    #len_of_vector = np.linalg.norm(vector)
    len_of_vector = np.sqrt(np.sum([v**2 for v in vector]))
    return len_of_vector
vector = np.array([-2,4,9,21])
result1 = compute_vector_length([vector])
print(round(result1,2))

def comput_dot_product(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result = result + vector1[i]*vector2[i]
    return result
v1 = np.array([0,1,-2,2])
v2 = np.array([2,5,1,0])
result2 = comput_dot_product(v1,v2)
print(round(result2,2))

x = np.array([[1,2],[3,4]])
k = np.array([1,2])
print("result \n", x.dot(k))

x1 = np.array([[-1,2],[3,-4]])
k1 = np.array([1,2])
print("result \n", x1@k1)

def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result
m = np.array([[-1,1,1], [0,-4,9]])
v = np.array([0,2,1])
result5 = matrix_multi_vector(m,v)
print(result5)

m1 = np.array([[0, 1, 2], [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result6 = matrix_multi_vector(m1,m2)
print(result6)

m3 = np.eye(3) #tạo ra một ma trận đơn vị 3x3
m4 = np.array([[1,1,1], [2,2,2], [3,3,3]])
result7 = m3@m4
print(result7)

m5 = np.eye(2) 
m5 = np.reshape(m5, (-1,4)[0])
m6 = np.array([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]])
result8 = m5@m6
print(result8)

m7 = np.array([[1,2], [3,4]])
#C: đọc theo hàng, từ trái sang phải, rồi xuống hàng tiếp theo.
#F: đọc theo cột, từ trên xuống dưới, rồi sang cột tiếp theo.
m7 = np.reshape(m7, (-1,4), "F")[0] 
m8 = np.array([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]])
result9 = m7@m8
print(result9)

def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result
m9 = np.array([[-2,6], [8,-4]])
result10 = inverse_matrix(m9)
print(result10)

def compute_eigenvalues_eigenvectors(matrix):
    # Tính toán giá trị riêng và vector riêng
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues , eigenvectors
matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(eigenvectors)
def compute_cosine(v1,v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    cos_sim = dot_product/(norm_v1*norm_v2)
    return cos_sim
x = np.array([1,2,3,4])
y = np.array([1,0,3,0])
result12 = compute_cosine(x,y)
print(round(result12,3))