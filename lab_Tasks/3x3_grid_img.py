import cv2
import numpy as np

img = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image6.png")
small = cv2.resize(img, (100, 100))

row = np.hstack((small, small, small))
grid = np.vstack((row, row, row))

cv2.imshow("3x3 Grid", grid)
cv2.waitKey(10000)
cv2.destroyAllWindows()
