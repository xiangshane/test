from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time (s)')
plt.show()
spectrum=triangle.make_spectrum()
print(spectrum.hs[0])