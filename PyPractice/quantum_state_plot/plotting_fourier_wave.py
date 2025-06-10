import numpy as np
class QuantumState:
    def __init__(self, amplitudes):
        self.amplitudes = np.array(amplitudes, dtype=complex)
        self.normalize()
    def normalize(self):
        norm = np.linalg.norm(self.amplitudes)
        self.amplitudes /= norm
    def __str__(self):
        return f"Quantum State: {self.amplitudes}"
# calling a Q State
state = QuantumState([1/np.sqrt(2), 1/np.sqrt(2)])
print(state)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# QS as a vector
quantum_state = np.array([0.70710678 + 0.j, 0.70710678 + 0.j])
# time points
t = np.linspace(0, 1, 500)
# wave function in time evolution
wave_function = quantum_state[0] * np.exp(2j * np.pi * 1 * t) + quantum_state[1] * np.exp(2j * np.pi * 2 * t)
# fourier transform
fft_result = np.fft.fft(wave_function)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])
# Plotting
plt.figure(figsize=(12, 6))
#wave function plot
plt.subplot(2, 1, 1)
plt.plot(t, np.real(wave_function), label='Real part')
plt.plot(t, np.imag(wave_function), label='Imaginary Part', linestyle='--')
plt.title('Wave Function')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
# Fourier Transform plot
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.title('Fourier Transform')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
