import pyaudio
import wave
import sys
import os
 
_format = pyaudio.paInt16
_channels = 2
_rate = 44100
_chunk = 2048

audio = pyaudio.PyAudio()
seconds = 5

seconds = sys.argv[1]
file_output_title = sys.argv[2]
sec = int(seconds)

# Iniciar Stream
stream = audio.open(format=_format, 
                channels=_channels,
                rate=_rate, 
                input=True,
                frames_per_buffer=_chunk)

#os.system("clear")

print ("Grabando...");
frames = []
cron = 0

for i in range(0, int(_rate / _chunk * sec)):
    data = stream.read(_chunk);
    frames.append(data)
    
    if (((_chunk/_rate)*i) > cron):
      cron = cron + 1
      print (cron)
      
    
print ("Grabación Completa")
 
 
print(type(frames[1]))  
 
# Terminar Stream
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(file_output_title, 'wb')
waveFile.setnchannels(_channels)
waveFile.setsampwidth(audio.get_sample_size(_format))
waveFile.setframerate(_rate)
waveFile.writeframes(b''.join(frames))
waveFile.close()
