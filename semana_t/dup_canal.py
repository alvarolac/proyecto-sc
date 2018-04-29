""" 
  - Clonar el canal izquierdo en el derecho
  - Seminario de Computacion
  - Semana Tecnologica
  - Alvaro Araujo
  
"""
import pyaudio
import wave
import sys
import os
import numpy as np
from matplotlib import pyplot as plt

_format = pyaudio.paInt16
_channels = 2
_rate = 44100
_chunk = 2048

if len(sys.argv) < 3:
    print("Syntax: %s entrada.wav salida.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

audio = pyaudio.PyAudio()

#stream = audio.open(format=_format,
#                channels=_channels,
#                rate=_rate,
#                output=True, 
#                frames_per_buffer=_chunk)

data = wf.readframes(_chunk)
frames = []
os.system("clear")

while len(data) > 0:
    data_num = np.fromstring(data,dtype=np.int16)
    data_num[1::2] = data_num[0::2]
    
    #stream.write(data)
    frames.append(data_num)
    data = wf.readframes(_chunk)

audio.terminate()

waveFile = wave.open(sys.argv[2], 'wb')
waveFile.setnchannels(_channels)
waveFile.setsampwidth(audio.get_sample_size(_format))
waveFile.setframerate(_rate)
waveFile.writeframes(b''.join(frames))
waveFile.close()

print("\n--------------------------------------------------------------")
print("Archivo Generado! Salida --> %s" % sys.argv[2])
print("--------------------------------------------------------------\n")

