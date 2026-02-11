import cv2

img = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image1.png")

cv2.putText(
    img,
    "Hello OpenCV",
    (50, 100),                
    cv2.FONT_HERSHEY_SIMPLEX,
    1,                        
    (0, 255, 0),              
    2                         
)

cv2.imshow("Text Image", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
