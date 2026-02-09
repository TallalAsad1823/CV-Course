import cv2

img = cv2.imread("photo.jpg")

# Draw a rectangle: (Image, Top-Left, Bottom-Right, Color, Thickness)
# Color is in BGR format (255, 0, 0) is Blue
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

# Add text labels
cv2.putText(img, "Object Found", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Drawing", img)
cv2.waitKey(0)