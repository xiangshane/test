from thinkdsp import Sinusoid
from thinkdsp import normalize,unbias
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
square=SquareSignal(1100).make_wave(duration=0.5,framerate=10000)
square.make_audio()
square.write(filename='Square.wav')
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()
