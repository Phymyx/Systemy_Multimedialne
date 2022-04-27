import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys


def RLE_encoding(img):
    encoded = []
    width = img.shape[1]
    height = img.shape[0]
    if len(img.shape) == 3:
        depth = img.shape[2]
        encoded.append((height, width, depth))
    else:
        encoded.append((height, width))
    flat = img.flatten()
    zlicz = 0
    prev = None
    for pixel in flat:
        if prev == None:
            prev = pixel
            zlicz += 1
        else:
            if prev != pixel:
                encoded.append((zlicz, prev))
                prev = pixel
                zlicz = 1
            else:
                if zlicz < (2**8) - 1:
                    zlicz += 1
                else:
                    encoded.append((zlicz, prev))
                    prev = pixel
                    zlicz = 1
    encoded.append((zlicz, prev))
    outp = np.array(encoded, dtype=object)
    return outp


def RLE_decode(encoded):
    decoded = []
    s = (encoded[0])
    for i in encoded[1:]:
        zlicz, pix = i[0], i[1]
        decoded.extend([pix] * zlicz)
    outp = np.array(decoded).reshape(s)
    return outp


def comparsion(imgu, enc):
    before = sys.getsizeof(imgu) / 1024
    print("przed kompresja: ", before)
    after = sys.getsizeof(enc) / 1024
    print("po kompresji: ", after)
    CR = abs(before)/abs(after)
    procent = after/before*100
    print("procent kompresji: ", round(procent, 2), "%")
    return CR


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj,np.ndarray):
        size=obj.nbytes
    elif isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def comp2(img2, enc2):
    bef = get_size(img2)
    print("przed kompresja: ", bef)
    af = get_size(enc2)
    print("po kompresji: ", af)
    CR = abs(get_size(img2))/abs(get_size(enc2))
    procent = af / bef * 100
    print("procent kompresji: ", round(procent, 2), "%")
    return CR


def check(original, duplicate):
    if len(original.shape) == 3:
        if original.shape == duplicate.shape:
            h, w, depth = original.shape
            for d in range(depth):
                for y in range(h):
                    for x in range(w):
                        if original[y][x][d] == duplicate[y][x][d]:
                            pass
                        else:
                            print("nie sa takie same")
                            return
        print("obrazy sa takie same")
    else:
        if original.shape == duplicate.shape:
            h, w = original.shape
            for y in range(h):
                for x in range(w):
                    if original[y][x] == duplicate[y][x]:
                        pass
                    else:
                        print("nie sa takie same")
                        return
        print("obrazy sa takie same")


img = cv2.imread("techniczny.jpg")
encoded = RLE_encoding(img)
decoded = RLE_decode(encoded)

#output = comparsion(img, encoded) #moje
output = comp2(img, encoded) #obliczenia rozmiaru z pdfa
print("stopien kompresji: ", output)

check(img, decoded)
