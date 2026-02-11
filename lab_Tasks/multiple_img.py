import cv2

img = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image6.png")

cv2.imshow("Window1", img)
cv2.imshow("Window2", img)

cv2.waitKey(10000)
cv2.destroyAllWindows()
