from thinkdsp import Sinusoid
from thinkdsp import normalize,unbias
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
triangle = TriangleSignal().make_wave(duration=0.01)
#triangle.plot()
#decorate(xlabel='Time (s)')
#plt.show()

spectrum = triangle.make_spectrum()
#print(spectrum.hs[0])
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
plt.show()
wave=SquareSignal(freq=440).make_wave(duration=0.5)
wave=SawtoothSignal(freq=440).make_wave(duration=0.5)