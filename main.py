import numpy as np
import matplotlib.pyplot as plt


def get_array():
    x_len = int(input('Number of columns:'))
    y_len = int(input('Number of rows:'))

    arr = []
    for y in range(x_len):
        row = []
        for x in range(y_len):
            row.append(float(input().strip()))
        arr.append(row)

    return arr


signal = get_array()

spectrum = np.fft.fft2(signal)
magnitude = np.abs(spectrum)
phase = np.angle(spectrum)

plt.subplot(2, 2, 1)
plt.imshow(signal, cmap='jet')
plt.title('signal')

plt.subplot(2, 2, 2)
plt.imshow(magnitude, cmap='jet')
plt.title('amplitude spectrum')

"""
plt.subplot(2, 3, 3)
plt.imshow(phase, cmap='jet')
plt.title('phase spectrum')
"""

r, c = spectrum.shape
fraction = 0.1
spectrum[int(r*fraction):int(r*(1-fraction))] = 0
spectrum[:, int(c*fraction):int(c*(1-fraction))] = 0

plt.subplot(2, 2, 3)
plt.imshow(np.abs(spectrum), cmap='jet')
plt.title('filtered spectrum')

inverse = np.fft.ifft2(spectrum).real

plt.subplot(2, 2, 4)
plt.title('inverse')
plt.imshow(inverse, cmap='jet')

plt.show()
