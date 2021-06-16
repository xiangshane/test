from thinkdsp import SawtoothSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt

def filter_spectrum(spectrum):
    spectrum.hs[1:]/=spectrum.fs[1:]
    spectrum.hs[0]=0
wave=SawtoothSignal(freq=440).make_wave(duration=0.5)
spectrum=wave.make_spectrum()
spectrum.plot(high=10000,color='gray')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')
plt.show()