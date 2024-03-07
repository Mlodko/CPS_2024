import numpy as np
import matplotlib.pyplot as plt

## Parameters 
AMPLITUDE = 230
SINE_FREQ = 50
SIMULATION_TIME = 1

## Preparing the functions
sine = lambda t: AMPLITUDE * np.sin(SINE_FREQ * t)
def sinc(t):
    if t == 0:
        return 1
    return np.sin(t) / t

## Analog
ANALOG_FREQ = 1_000_000
analog_t = np.arange(0, SIMULATION_TIME, 1/ANALOG_FREQ)
analog_y = sine(analog_t)

## Sampling the sine
SAMPLING_FREQ = 200
sampled_t = np.arange(0, SIMULATION_TIME, 1/SAMPLING_FREQ)
sampled_y = sine(sampled_t)

## Reconstruction
RECONSTRUCTION_FREQ = 10_000

reconstructed_t = np.arange(0, SIMULATION_TIME, 1/RECONSTRUCTION_FREQ)
reconstructed_y = np.zeros(len(reconstructed_t))

for r_index in range(len(reconstructed_y)):
    sum = 0

    for k in range(len(sampled_y)):
        m = np.pi * SAMPLING_FREQ * (sampled_t[k] - reconstructed_t[r_index])

        sum += sampled_y[k] * sinc(m)

    reconstructed_y[r_index] = sum

fig, ax = plt.subplots()
ax.plot(analog_t, analog_y, 'b-',
        reconstructed_t, reconstructed_y, 'r-')
plt.show()

    