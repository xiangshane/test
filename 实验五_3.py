import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate
from thinkdsp import SinSignal

from thinkdsp import Chirp
from thinkdsp import normalize, unbias
PI2 = 2 * np.pi
class SawtoothChirp(Chirp):
    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys
signal = SawtoothChirp(start=2500, end=3000)
wave = signal.make_wave(duration=1, framerate=20000)
wave.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()
# wave.make_audio()
# wave.write(filename='112.wav')