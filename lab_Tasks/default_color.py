import cv2

img_color = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image6.png", 1)  # 1 = Color
cv2.imshow("Color Image", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
