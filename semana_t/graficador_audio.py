""" 
  - Graficar valores de un audio (estereo)
  - Seminario de Computacion
  - Semana Tecnologica
  - Alvaro Araujo
  
"""
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1],'r')

signal = wf.readframes(-1)
signal = np.fromstring(signal,dtype=np.int16)


plt.figure(1)

plt.subplot(2,1,1)
plt.title('Canal Izquierdo')
plt.plot(signal[0::2])

plt.subplot(2,1,2)
plt.title('Canal Derecho')
plt.plot(signal[1::2])

plt.show()
