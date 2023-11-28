import scipy.io.wavfile as wavfile
import scipy
import scipy.fft
from scipy.signal import argrelextrema
import numpy as np
from matplotlib import pyplot as plt

plt.title("Plein Jeu V/Stopped Diapason 8 - A")
fs_rate, signal = wavfile.read("chords/PleinJeuV_StoppedDiapason8/A.wav")

# Determine sampling frequency
print(f"Frequency sampling: {fs_rate} Hz")

print(" ")

# Determine number of time samples in the wav file
N = signal.shape[0]
print(f"N| Number of time samples: {N}")

# Determine audio clip length
secs = N / float(fs_rate)
print(f"Number of seconds: {round(secs, 3)}")

# Determine amount of time between each sample
time_step = 1 / fs_rate
print(f"Time between each sampling interval {time_step}")

# Create a range of times for DFT
time_range = np.arange(0, secs, time_step)

# Compute DFT through FFT algorithm
FFT = abs(scipy.fft.fft(signal))[range(N // 2)]


# Compute DFT sample frequencies
freqs = scipy.fft.fftfreq(signal.size, time_range[1]-time_range[0])[range(N // 2)]

# Axes
xvals = []
yvals = []

# Cut down data to avoid excess noise
for entry in range(len(FFT)):
    if freqs[entry] < 500 or freqs[entry] > 4000:
        pass
    else:
        xvals.append(freqs[entry])
        yvals.append(FFT[entry])

# Find the maxima
fft_maxima = argrelextrema(FFT, np.greater)
# Print out each maxima
for maximum in fft_maxima[0]:
    if FFT[maximum] > 600000 and freqs[maximum] > 500:
        plt.axvline(x=freqs[maximum], color='b')
        print(f"Outstanding Frequency: {round(freqs[maximum])}")

# Graph
plt.xlim(500,4000)
p2 = plt.plot(xvals, yvals, "r") # plotting the complete fft spectrum
plt.xlabel('Frequency (Hz)')
plt.ylabel('Weight of frequency')
plt.show()
