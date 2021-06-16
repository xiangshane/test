import os

from matplotlib.pyplot import subplot
from thinkdsp import SquareSignal
from thinkdsp import decorate
from thinkdsp import plt
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
from thinkdsp import SinSignal
from thinkdsp import read_wave

square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)
square.make_spectrum().plot()
segment=SinSignal(10000).make_wave(duration=0.5, framerate=10000).make_audio()
segment.write(filename='fb.wav')
# decorate(xlabel='Frequency (Hz)')

# plt.show()