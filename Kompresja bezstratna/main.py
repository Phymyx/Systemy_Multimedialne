import numpy as np

test = np.array([[0, 0, 1, 1, 2],
                [2, 1, 3, 4, 1],
                [2, 3, 4, 2, 2],
                [1, 3, 1, 3, 3],
                [2, 4, 4, 1, 4],
                [3, 1, 3, 1, 2]])


def RLE_koder(macierz):
    height = macierz.shape[0]
    print(height)
    vec = macierz.flatten()
    print(vec)
    width = vec.shape[0]
    print(width)
    new_vec = []
    new_vec.append(height)
    print(new_vec)
    licznik = 1
    for i in range(width-1):

        print("i:")
        print(i)
        if vec[i] == vec[i+1]:
            licznik += 1
            print(licznik)
        else:
            new_vec.append(licznik)
            new_vec.append(vec[i-licznik+1])
            licznik = 1
            print("koniec podobnych")
            print(licznik)


            #print(licznik)

            #new_vec.append(licznik)






RLE_koder(test)
