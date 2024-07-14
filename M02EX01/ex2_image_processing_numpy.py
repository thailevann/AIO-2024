
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread("./image/dog.jpeg")

#convert rgb to gray image using Lightness method
#(max(R,G,B)+ min(R,G,B))/2
def qs12_rgb2gray_lightness(img):
    return np.mean([np.max(img, axis = -1), np.min(img, axis = -1)], axis = 0)
#convert rgb to gray image using Average method
#(R+G+B)/3
def qs13_rgb2gray_average(img):
    return np.mean(img, axis = -1)

#convert rgb to gray image using Luminosity method
#0.21*R + 0.72*G + 0.07*B
def qs13_rgb2gray_luminosity(img):
    return np.dot(img[..., :3], [0.21, 0.72, 0.07]) # trích xuất tất cả các phần tử trong mảng theo các chiều chiều cao và chiều rộng của hình ảnh, và chỉ lấy 3 kênh màu đầu tiên (R, G, B).

#question 12
gray_img_01 = qs12_rgb2gray_lightness(img)
print(gray_img_01 [0 , 0])

#question 13
gray_img_01 = qs13_rgb2gray_average(img)
print(gray_img_01 [0 , 0])

#question 14
gray_img_01 = qs13_rgb2gray_luminosity(img)
print(gray_img_01 [0 , 0])

