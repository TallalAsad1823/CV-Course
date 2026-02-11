import cv2

# Read image
img = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image1.png")

# Show image
cv2.imshow("UIIT", img)

# Wait for 10 seconds (10000 ms)
cv2.waitKey(10000)

# Close window
cv2.destroyWindow("UIIT")
