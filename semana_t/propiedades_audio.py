""" 
  - Consultar informacion wav
  - Seminario de Computacion
  - Semana Tecnologica
  - Alvaro Araujo

"""
import pyaudio
import wave
import sys
import os
import numpy as np

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
print("\n----------- Audio Properties -----------")
print(" - Rate:           %s Hz" % wf.getframerate())
print(" - Format:         %s" % audio.get_format_from_width(wf.getsampwidth()))
print(" - Chunck:         %d" % int(2*(2**8) * wf.getnchannels() * (16)/8))
print(" - Channels:       %s" % wf.getnchannels())
print(" - Sample Width:   %s bytes" % wf.getsampwidth())
print(" - Number Frames:  %s" % wf.getnframes())
print("----------------------------------------\n")

stream.stop_stream()
stream.close()
audio.terminate()
