import matplotlib.pyplot as plt
import numpy as np


def chunk_arr(arr, bits):
    tablica = np.zeros(255)
    print(len(tablica))
    #size = np.unique(arr).size
    size1 = len(tablica)
    print(size1)
    if bits < size1:
        chunk_size = bits * 2
        print("good")
        new_size = int(size1/chunk_size)
        print(new_size)

    else:
        print("not good")


def change_bit(F):
    '''
    A = <0,1>
    B = <0, d> d-l.dodatnia
    C = <m,n> n-l.dod, m<n & m-moze byc mniejsze od0

    A = Za
    B = Zb
    C = Zc

    Za = (Zb/d) = (Zc - m)/(n-m)
    Zb = Za * d
    Zc = (Za * (n-m))+m

    uint8 <0,255> to bedzie

    :return:
    '''
    Za = (F+1)/2 #F<0,1>
    Zc = Za * 65535 - 32768
    outp = int(Zc)
    return outp


def bit_res(dzwiek, wybor):
    '''
    type = dzwiek.dtype
    min1 = np.iinfo(np.int32).min
    max1 = np.iinfo(np.int32).max
    zakres = np.unique(dzwiek).size
    np.issubdtype(dzwiek.dtype, np.integer)
    np.issubdtype(dzwiek.dtype, np.float)
    '''
    #sprawdzenie jaki to typ danych
    typ = dzwiek.dtype
    if typ == np.float32:
        m = -1
        n = 1
    elif typ == np.int32:
        m = np.iinfo(np.int32).min
        n = np.iinfo(np.int32).max
    elif typ == np.int16:
        m = np.iinfo(np.int16).min
        n = np.iinfo(np.int16).max
    elif typ == np.int8:
        m = np.iinfo(np.int8).min
        n = np.iinfo(np.int8).max
    elif typ == np.uint8:
        m = np.iinfo(np.uint8).min
        n = np.iinfo(np.uint8).max
    else:
        print("bledna wartosc typu")
    #testo = np.iinfo(np.wybor).min
    
    Za = (dzwiek - (m))/(n - m)
    print(Za)

    if wybor == np.float32:
        m1 = -1
        n1 = 1
        Zc = [Za * (n1 - m1)] + m1

    elif wybor == np.int32:
        m1 = np.iinfo(np.int32).min
        n1 = np.iinfo(np.int32).max
        Zc = [Za * (n1 - m1)] + m1
    elif wybor == np.int16:
        m1 = np.iinfo(np.int16).min
        n1 = np.iinfo(np.int16).max
        Zc = Za * (n1 - m1) + m1
        Zc = Zc.astype(int)
        print(Zc)
    elif wybor == np.int8:
        m1 = np.iinfo(np.int8).min
        n1 = np.iinfo(np.int8).max
        Zc = Za * (n1 - m1) + m1
        Zc = Zc.astype(int)
        print(Zc)
    elif wybor == np.uint8:
        m1 = np.iinfo(np.uint8).min
        n1 = np.iinfo(np.uint8).max
        Zc = [Za * (n1 - m1)] + m1
    else:
        print("bledna wartosc typu")


arr = [2, 10, 40, 150]
#ints = np.array([.1, .3, .6, .9], dtype=np.float32)
ints = np.array(arr, dtype=np.uint8)
y = bit_res(ints, np.int8)
x = np.round(np.linspace(0,255,255,dtype=np.uint8))


tab = [0, 255]
chunk_arr(tab, 1)


'''
x = np.round(np.linspace(0,255,255,dtype=np.uint8))
x1 = np.round(np.linspace(0,255,255,dtype=np.uint8))
plt.plot(x, x1)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph')
plt.show()
'''



'''
ints = np.array([1, 2, 3], dtype=np.float32)
print(ints.dtype)
x = ints.dtype

if x == np.float32:
    print("czesc to flaot32")
else:
    print("to nie float32")

xd = np.issubdtype(ints.dtype, np.integer)
if xd == True:
    print("elo")
else:
    print("nara")

print(xd)
y = ints.dtype

#print(np.iinfo().min)
'''
