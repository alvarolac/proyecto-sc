""" 
  - Reproductor de audio con parametros automaticos
  - Seminario de Computacion
  - Semana Tecnologica
  - Alvaro Araujo

"""
import pyaudio
import wave
import sys
import os
import numpy as np

_format = pyaudio.paInt16
_channels = 2
_rate = 44100
_chunk = 2048

maxValue = 2**16
bars = 50

if len(sys.argv) < 2:
    print("Syntax: %s entrada.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

audio = pyaudio.PyAudio()


np.seterr(all='ignore')

stream = audio.open(format=_format,
                channels=_channels,
                rate=_rate,
                output=True)

os.system("clear")

data = wf.readframes(_chunk)

while len(data) > 0:

    stream.write(data)
    data_visual = np.fromstring(data,dtype=np.int16)
    dataL = data_visual[0::2]
    dataR = data_visual[1::2]
    
    data = wf.readframes(_chunk)
    
    if(len(dataL)==0 or len(dataR)==0):
      break
      
    peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue;
    peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue;
  
    lString = "|"*int(peakL*bars)+" "*int(bars-peakL*bars)
    rString = "|"*int(peakR*bars)+" "*int(bars-peakR*bars)
    print("L=[%s] R=[%s]"%(lString, rString))


stream.stop_stream()
stream.close()

audio.terminate()
