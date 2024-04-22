import cv2
import numpy as np

# load images
image1 = cv2.imread("image1.png")
image2 = cv2.imread("image2.png")
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
# compute difference
difference = cv2.subtract(image1, image2)

# convert the difference to grayscale
Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

# if there is a difference, the sum will be greater than 0
if np.sum(Conv_hsv_Gray) > 0:
    print("There is a difference between the two images.")
else:
    print("There is no difference between the two images.")
