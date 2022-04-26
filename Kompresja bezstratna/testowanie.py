import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
import os


test = np.array([[1, 1, 4, 4, 5],
                 [6, 5, 5, 2, 2],
                [2, 2, 2, 2, 4],
                [1, 2, 3, 3, 3]])


def show(img, figsize=(10, 10), title="Image"):
    figure=plt.figure(figsize=figsize)

    plt.imshow(img)
    plt.show()


dummy = np.random.randint(0, 255, (100, 100)).astype(np.uint8)
#show(dummy)

print("oryginalny: ", sys.getsizeof(dummy)/1024)

#cv2.imwrite("d.png", dummy) #zapis dummiego

img = cv2.imread("d.png", 0)

print("odcien szarosci: ", sys.getsizeof(img)/1024)

dd = np.zeros((100, 100)).astype(np.uint8)
#show(dd)

print("blank: ", sys.getsizeof(dd)/1024)

#cv2.imwrite("dd.png", dd)


def get_size(filename="dd.png"):
    stat = os.stat(filename)
    size = stat.st_size
    return size


print(get_size())
print(get_size("d.png"))


def RLE_encoding(img, bits=8, binary=False, view=False):
    if binary:
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    if view:
        show(img)

    encoded = []
    shape = img.shape
    count = 0
    prev = None
    fimg = img.flatten()
    th = 127
    for pixel in fimg:
        if binary:
            if pixel < th:
                pixel = 0
            else:
                pixel = 1
        if prev == None:
            prev = pixel
            count += 1
        else:
            if prev != pixel:
                encoded.append((count, prev))
                prev = pixel
                count = 1
            else:
                if count < (2**bits) - 1:
                    count += 1
                else:
                    encoded.append((count, prev))
                    prev = pixel
                    count = 1
    encoded.append((count, prev))

    return np.array(encoded)


fpath = "bg20.png"
img = cv2.imread(fpath, 0)
shape = img.shape
encoded = RLE_encoding(img, bits=8)
print(encoded)


def RLE_decode(encoded, shape):
    decoded = []
    for rl in encoded:
        r, p = rl[0], rl[1]
        decoded.extend([p]*r)
    dimg = np.array(decoded).reshape(shape)
    return dimg


dimg = RLE_decode(encoded, shape)
#show(dimg)


shape_test = test.shape
encoded_test = RLE_encoding(test, bits=8)
print(encoded_test)

decoded_test = RLE_decode(encoded_test, shape_test)
print(decoded_test)
