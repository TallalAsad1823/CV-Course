import cv2 

# 1. Load the image
img = cv2.imread("photo.jpg") 

# 2. Show the image in a window
cv2.imshow("My Window", img)

# 3. Wait for any key press to close the window
cv2.waitKey(0) 
cv2.destroyAllWindows()