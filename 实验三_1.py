import winsound
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate
from winsound import PlaySound
wave = read_wave('t4.wav')
wave.make_audio()
start = 1.2
duration = 0.6
segment = wave.segment(start, duration)
spectrum = segment.make_spectrum()
decorate(xlabel='Frequency (Hz)')
#spectrum.low_pass(3000)
# spectrum.high_pass(3000)
spectrum.band_stop(3000,6000)
# spectrum.plot(high=7000)
segment=spectrum.make_wave()
segment.write(filename='band_stop.wav')
# def stretch(wave, factor):
#     wave.ts *= factor
#     wave.framerate /= factor
# stretch(segment, 0.5)
# segment.make_audio()
# segment.plot()
# plt.show()