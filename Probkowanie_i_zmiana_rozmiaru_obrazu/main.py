import numpy as np
import cv2
import matplotlib.pyplot as plt

imgGray = cv2.imread('img.jpeg', 0)

if (len(imgGray.shape)<3):
    print("grey")
else:
    print("rgb")

print(type(imgGray))
print(imgGray.shape)

h, w = imgGray.shape
print('width:  ', w)
print('height: ', h)
# width:   332
# height:  300

def scaleup(img, scale, method):
    width, height = img.size
    print(width)
    print(height)


#scaleup(img, 0, 0)

'''
    def nearestNeighborScaling(source, newWid, newHt):
        target = makeEmptyPicture(newWid, newHt)
        width = getWidth(source)
        height = getHeight(source)
        for x in range(0, newWid):
            for y in range(0, newHt):
                srcX = int(round(float(x) / float(newWid) * float(width)))
                srcY = int(round(float(y) / float(newHt) * float(height)))
                srcX = min(srcX, width - 1)
                srcY = min(srcY, height - 1)
                tarPix = getPixel(target, x, y)
                srcColor = getColor(getPixel(source, srcX, srcY))
                setColor(tarPix, srcColor)

        return target
'''
