import numpy as np
import matplotlib.pyplot as plt

## Parameters 
amplitude = 230
sine_freq = 50
simulation_time = 1
sampling_freqs = [
    (10_000, 'b-'),
    (51, 'g-o'),
    (50, 'r-o'),
    (49, 'k-o')
]

## Preparing the sine
sine = lambda t: amplitude * np.sin(t * sine_freq)

## Simulation and plotting
fig, ax = plt.subplots()

for freq in sampling_freqs:
    t = np.arange(0, simulation_time, 1/freq[0])
    y = sine(t)
    ax.plot(t, y, freq[1])

plt.show()
