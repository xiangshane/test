from thinkdsp import Sinusoid
from thinkdsp import normalize,unbias
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

class SawtoothSignal(Sinusoid):
    def evaluate(self,ts):

        cycles = self.freq *ts+self.offset/np.pi/2
        frac,_=np.modf(cycles)
        ys=normalize(unbias(frac),self.amp)
        return ys
sawtooth = SawtoothSignal().make_wave(duration=0.5,framerate=40000)
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
sawtooth.make_spectrum().plot(color='gray')
square=SquareSignal(amp=0.5).make_wave(duration=0.5,framerate=40000)
square.make_spectrum().plot()
# triangle=TriangleSignal(amp=0.79).make_wave(duration=0.5,framerate=40000)
# triangle.make_spectrum().plot()
plt.show()
