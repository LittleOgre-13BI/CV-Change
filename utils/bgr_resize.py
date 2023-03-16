import cv2
import os

size = (768, 1024)
bgr_path = 'Images/bgr'
bgrs = os.listdir(bgr_path)

for i in range(5):
    bgr = cv2.imread(os.path.join(bgr_path, bgrs[i]))
    bgr = cv2.resize(src=bgr, dsize=size)
    cv2.imshow("bgr", bgr)
    key = cv2.waitKey(10000)
    if key == 27:
        continue