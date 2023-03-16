import cv2
import os


path = "Images/person"
save_path = "Images/output_person"
size = (576, 1024)
images = os.listdir(path)

for image in images:
    img_in = cv2.imread(path + "/" + image)
    img_temp = cv2.resize(img_in, size)
    for _ in range(48):
        img_temp = cv2.copyMakeBorder(img_temp, 0, 0, 2, 2, cv2.BORDER_REFLECT)
    cv2.imwrite(save_path + "/" + image, img_temp)