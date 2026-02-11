import cv2
import os

path = r"/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images" # Apna folder path daalna

files = os.listdir(path)

for name in files:
    if name.lower().endswith(('.jpg', '.png')):
        full_path = os.path.join(path, name)
        img = cv2.imread(full_path)
        img = cv2.resize(img, (400, 400))
        
        cv2.imshow("Slide Show", img)
        cv2.waitKey(1000)   # 1 second per image

cv2.destroyAllWindows()
