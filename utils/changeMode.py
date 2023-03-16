from PIL import Image
import cv2 as cv
import os


def PNG_JPG(PngPath):
    img = cv.imread(PngPath, 0)
    w, h = img.shape[::-1]
    infile = PngPath
    outfile = os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('L').save(outfile, quality=100)
            os.remove(PngPath)
        else:
            img.convert('L').save(outfile, quality=100)
            os.remove(PngPath)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误", e)

img_dir = os.listdir('Images/cloth-mask')
for img in img_dir:
    if img.endswith('.png'):
        PNG_JPG('Images/cloth-mask/' + img)



