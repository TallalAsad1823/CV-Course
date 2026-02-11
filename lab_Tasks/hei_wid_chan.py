import cv2

img = cv2.imread("/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image4.png")

print(img.shape)




# import cv2
# import numpy as np

# # Load image
# img_path = "/Users/rufaeelasad/Desktop/Computer Vision /CV-Codes/lab_Tasks/images/image6.png"
# img = cv2.imread(img_path)

# if img is None:
#     print(f"Image not found: {img_path}")
#     exit()

# # Get image details
# height, width, channels = img.shape
# info_text = f"Height: {height} px   Width: {width} px   Channels: {channels}"

# # Create a panel below the image
# panel_height = 50
# panel = np.zeros((panel_height, width, 3), dtype=np.uint8)  # Black background
# panel[:] = (50, 50, 50)  # Dark gray background

# # Put text in the center of the panel
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 1
# color = (0, 255, 0)  # Green
# thickness = 2

# # Calculate text size and position to center it
# (text_width, text_height), _ = cv2.getTextSize(info_text, font, font_scale, thickness)
# x = (width - text_width) // 2
# y = (panel_height + text_height) // 2

# cv2.putText(panel, info_text, (x, y), font, font_scale, color, thickness)

# # Stack image on top of panel
# output = np.vstack((img, panel))

# # Show
# cv2.imshow("Image Info", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
