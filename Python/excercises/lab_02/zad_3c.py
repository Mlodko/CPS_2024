import numpy as np
import matplotlib.pyplot as plt

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

def create_IDCT_matrix(size):
    return create_DCT_matrix(size).transpose()

N = 100
SAMPLING_FREQ = 1000

t = np.arange(0, N * 1/SAMPLING_FREQ, 1/SAMPLING_FREQ)

sine_1 = lambda x: 50 * np.sin(x * 52.5)
sine_2 = lambda x: 100 * np.sin(x * 102.5)
sine_3 = lambda x: 150 * np.sin(x * 152.5)

signal = np.zeros(N)

for i in range(N):
    current_time = t[i]
    signal[i] = sine_1(current_time) + sine_2(current_time) + sine_3(current_time)

fig, ax = plt.subplots()
ax.grid()
ax.plot(t, signal, 'b-o',
        t, sine_1(t), '--',
        t, sine_2(t), '--',
        t, sine_3(t), '--')
plt.show()

dct = create_DCT_matrix(N)
idct = create_IDCT_matrix(N)

if(False):
    for i in range(N):
        print(f"i = {i}\n{dct[i]}\n{idct[:,i]}")


y = np.matmul(dct, signal)
f = np.arange(0, N) * SAMPLING_FREQ / N

fig, ax = plt.subplots()
ax.grid()
ax.stem(f, y)
plt.show()

reconstructed_signal = np.matmul(idct, y)

fig, ax = plt.subplots()
ax.grid()
ax.plot(t, signal, 'b-o',
        t, reconstructed_signal, 'r--x')
plt.show()


