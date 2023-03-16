import cv2
import os
import numpy as np

person_path = 'Images/output'
persons = os.listdir(person_path)
person_mask_path = 'Images/person-mask'
person_masks = os.listdir(person_mask_path)
bgr_path = 'Images/bgr'
bgrs = os.listdir(bgr_path)
save_path = 'Images/final'
size = (768, 1024)

for i in range(5):
    person = cv2.imread(os.path.join(person_path, persons[i]))
    person_mask = cv2.imread(os.path.join(person_mask_path, person_masks[i]), 0)
    bgr = cv2.imread(os.path.join(bgr_path, bgrs[i]))
    bgr = cv2.resize(bgr, size)

    height, width, channel = person.shape
    b, g, r = cv2.split(person)

    bgr = bgr.transpose(2, 0, 1)
    dstt = np.zeros((3, height, width), dtype=person.dtype)

    for j in range(3):
        dstt[j][:, :] = bgr[j][:, :] * (255.0 - person_mask) / 255
        dstt[j][:, :] += np.array(person[:, :, j] * (person_mask / 255), dtype=np.uint8)
    cv2.imwrite(os.path.join(save_path, "0"+str(i)+".png"), cv2.merge(dstt))