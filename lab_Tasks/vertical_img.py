import cv2
import numpy as np

img = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image6.png")
resized_img = cv2.resize(img, (400, 200))

vertical = np.vstack((resized_img, resized_img))

cv2.imshow("Vertical", vertical)
cv2.waitKey(10000)
cv2.destroyAllWindows()
