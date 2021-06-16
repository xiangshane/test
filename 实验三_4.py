from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time (s)')
spectrum=triangle.make_spectrum()
spectrum.hs[0]=100
print(spectrum.hs[0])
triangle.plot()
triangle.plot(color='gray')
spectrum.make_wave().plot()
plt.show()