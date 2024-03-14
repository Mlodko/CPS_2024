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

dct = create_DCT_matrix(SIZE)
idct = np.linalg.inv(dct)

print(f'A:\n {dct}')
print(f'S:\n {idct}')
print(f'Teoretycznie identycznościowa:\n {np.round(np.matmul(idct, dct), 2)}')

x = np.random.randn(SIZE)

X = np.matmul(dct, x.transpose())
x_S = np.matmul(idct, X)
print(f'Średnia różnica sygnału po rekonstrukcji: {np.sum(abs(x-x_S)/SIZE)}')
