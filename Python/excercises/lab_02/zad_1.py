import numpy as np



def s(n, size):
    if n == 0:
        return np.sqrt(1/size)
    return np.sqrt(2/size)

def create_DCT_matrix(size):
    output_matrix = np.zeros((size, size))
    w = lambda k, n: s(k, size) * np.cos(np.pi * k/size * (n+0.5))
    for row in range(size):
        for column in range(size):
            output_matrix[row][column] = w(row, column)
    return output_matrix

SIZE = 4
MAX_ACCEPTABLE_ERROR = 10

dct = create_DCT_matrix(SIZE)
print(dct)
if_found = False
for vector in dct:
    for other_vector in dct:
        if np.array_equal(vector, other_vector):
            continue
        prod = np.sum(vector * other_vector)
        if round(prod, MAX_ACCEPTABLE_ERROR) != 0:
            print(prod)
            print(f'Wektory {vector} i {other_vector} nie są ortogonalne')
            if_found = True
            break
    if if_found:
        break
print('Wszystkie wektory macierzy są do siebie ortogonalne')




