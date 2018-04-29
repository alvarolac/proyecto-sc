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

max_v = 2**16
lon_bar = 60

if len(sys.argv) < 2:
    print("Syntax: %s entrada.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

audio = pyaudio.PyAudio()

stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

os.system("clear")

data = wf.readframes(_chunk)

while len(data) > 0:

    stream.write(data)
    data_num = np.fromstring(data,dtype=np.int16)
    data_num_l = data_num[0::2]
    data_num_r = data_num[1::2]
    
    data = wf.readframes(_chunk)
    
    if(len(data_num_l)==0 or len(data_num_r)==0):
      break
      
    cant_l = np.abs(int(np.max(data_num_l)) - int(np.min(data_num_l)))/int(max_v);
    cant_r = np.abs(int(np.max(data_num_r)) - int(np.min(data_num_r)))/int(max_v);
  
    bar_l = "|" * int(cant_l * lon_bar) + " " * int(lon_bar - cant_l * lon_bar)
    bar_r = "|" * int(cant_r * lon_bar) + " " * int(lon_bar - cant_r * lon_bar)
    print("L=[%s] R=[%s]" % (bar_l, bar_r))

stream.stop_stream()
stream.close()
audio.terminate()


