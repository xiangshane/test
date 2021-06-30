import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate
from thinkdsp import SinSignal
from thinkdsp import read_wave
from thinkdsp import Chirp
from thinkdsp import normalize, unbias
PI2=np.pi*2

class TromboneGliss(Chirp):
    def evaluate(self, ts):
        l1, l2 = 1.0 / self.start, 1.0 / self.end
        lengths = np.linspace(l1, l2, len(ts))
        freqs = 1 / lengths
        
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.cos(phases)
        return ys

wave = read_wave('87778__marcgascon7__vocals.wav')
wave.make_audio()
wave.make_spectrogram(1024).plot(high=1000)
# decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
high = 1000
# segment = wave.segment(start=1, duration=0.25)
# segment.make_spectrum().plot(high=high)
segment = wave.segment(start=3.5, duration=0.25)
segment.make_spectrum().plot(high=high)

decorate(xlabel='Frequency (Hz)')
plt.show()