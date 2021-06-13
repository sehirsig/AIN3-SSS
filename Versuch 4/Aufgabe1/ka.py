#!/usr/bin/env python3

import scipy.signal as win
import matplotlib.pyplot as plt
import numpy as np
import math


def mkchunks(arr, window_function, chunk_size):
    for i in range(0, len(arr) - chunk_size + 1, math.floor(chunk_size / 2)):
        yield np.concatenate([[0]*i, list(window_function(arr[i:i+chunk_size])), [0]*(len(arr) - (i + chunk_size))])


def windowed_fft(data):
    gauss_window = np.array(win.gaussian(512, 512 / 4))

    windows = np.array(list(mkchunks(data, lambda d: d * gauss_window, 512)))

    return np.fft.rfft(windows).mean(0)


def main():
    data = np.loadtxt("../../SoundV4/sound_data_6942018.csv", delimiter=",")

    data_fft = windowed_fft(data)
    freqs = np.fft.rfftfreq(len(data), 1 / 44100)
    limit = np.argmax(freqs > 1000)

    fig, ax = plt.subplots()
    ax.plot(freqs, np.abs(data_fft))
    fig.text(0.5, 0.04, 'Frequenz (Hz)', ha='center', va='center')
    fig.text(0.06, 0.5, 'Amplitude', ha='center', va='center', rotation='vertical')
    plt.show()


if __name__ == "__main__":
    main()

