import cv2

img = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image3.png")

resized_img = cv2.resize(img, (400, 200)) #width = 400, height = 200

cv2.imshow("Resized", resized_img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
