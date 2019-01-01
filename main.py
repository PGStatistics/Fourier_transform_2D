import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def get_array():
    x_len = int(input('Number of columns:'))
    y_len = int(input('Number of rows:'))

    arr = []
    for x in range(x_len):
        col = []
        for y in range(y_len):
            col.append(float(input().strip()))
        arr.append(col)

    return y_len, x_len, np.transpose(arr)


rows, cols, signal = get_array()

print('\nPerforming Fourier Transform...')
spectrum = np.fft.fft2(signal)
magnitude = np.abs(spectrum)
power = np.abs(spectrum) ** 2

# show signal
print('Generating signal colormap')
plt.imshow(signal, cmap='jet')
plt.savefig('signal.png', bbox_inches='tight')

# show amplitude and power spectrum
print('Generating amplitude and power spectra logarithmic colormaps...')
plt.subplot(1, 2, 1)
plt.imshow(magnitude, norm=LogNorm(vmin=5))
plt.title('amplitude spectrum')

plt.subplot(1, 2, 2)
plt.imshow(power, norm=LogNorm(vmin=5))
plt.title('power spectrum')

plt.savefig('spectrum.png', bbox_inches='tight')

print('Generating filtered spectrum...')
fraction = 0.1
filtered = spectrum.copy()
filtered[int(rows*fraction):int(rows*(1-fraction))] = 0
filtered[:, int(cols*fraction):int(cols*(1-fraction))] = 0

plt.subplot(1, 1, 1)
plt.imshow(np.abs(filtered), norm=LogNorm(vmin=5))
plt.title('filtered spectrum')
plt.savefig('filtered.png', bbox_inches='tight')

print('Performing inverse Fourier Transform...')
inverse = np.fft.ifft2(filtered).real

plt.title('inverse')
plt.imshow(inverse, cmap='jet')
plt.savefig('inverse.png', bbox_inches='tight')

print('Done!')