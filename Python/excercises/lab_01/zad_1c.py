import numpy as np
import matplotlib.pyplot as plt

## Parameters 
AMPLITUDE = 230
TIME_DURATION = 1
MAX_FREQ = 300
IF_SHOW_FIRST_PART: bool = False;
sine_freqs = np.arange(0, 300, 5)
sampling_freq, sampling_options = (100, 'r-o')
analog_freq, analog_options = (10_000, 'b-')

## First part
if IF_SHOW_FIRST_PART: 
    for index, freq in np.ndenumerate(sine_freqs):
        fig, ax = plt.subplots()
        sine = lambda t: AMPLITUDE * np.sin(freq * t)

        # Title
        ax.set(title=f'Iteration: {index[0] + 1}\nFrequency: {freq} Hz')
        ax.grid()

        # The "real" sine
        t = np.arange(0, TIME_DURATION, 1/analog_freq)
        y = sine(t)
        ax.plot(t, y, analog_options)

        # The sampled sine
        t = np.arange(0, TIME_DURATION, 1/sampling_freq)
        y = sine(t)
        ax.plot(t, y, sampling_options)

        plt.show()

## Second part

sine_freqs = [
    (5, 105, 205),
    (95, 105, 295),
    (95, 105)
]
colors = ['r-', 'g-', 'b-']

## Sine
for freqset in sine_freqs:
    fig, ax = plt.subplots()
    # Title
    ax.set(title=f'Sine frequencies: {freqset}')
    ax.grid()

    for index, freq in enumerate(freqset):
        sine = lambda t: AMPLITUDE * np.sin(t * freq)
        ## Analog
        t = np.arange(0, TIME_DURATION, 1/analog_freq)
        y = sine(t)
        ax.plot(t, y, colors[index] + '-')

        ## Sampling
        t = np.arange(0, TIME_DURATION, 1/sampling_freq)
        y = sine(t)
        ax.plot(t, y, colors[index])
    plt.show()

## Cosine
for freqset in sine_freqs:
    fig, ax = plt.subplots()
    # Title
    ax.set(title=f'Cosine frequencies: {freqset}')
    ax.grid()

    for index, freq in enumerate(freqset):
        cosine = lambda t: AMPLITUDE * np.cos(t * freq)
        ## Analog
        t = np.arange(0, TIME_DURATION, 1/analog_freq)
        y = cosine(t)
        ax.plot(t, y, colors[index] + '-')

        ## Sampling
        t = np.arange(0, TIME_DURATION, 1/sampling_freq)
        y = cosine(t)
        ax.plot(t, y, colors[index])
    plt.show()





