import pysinewave
import time

sinewave = pysinewave.SineWave(pitch = 12, pitch_per_second = 10)

sinewave.play()

time.sleep(3)