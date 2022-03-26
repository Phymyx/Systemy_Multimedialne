import wave

import matplotlib.pyplot as plt
import pyaudio
import numpy as np
import time
import soundfile as sf

audio = pyaudio.PyAudio()
numdevices = audio.get_device_count()
for i in range(0, numdevices):
    print(audio.get_device_info_by_index(i))

FORMAT = pyaudio.paInt16
CHANNELS = 1
FS = 44100
CHUNK = 1024

'''
stream = audio.open(input_device_index=0, format=FORMAT,
                    channels=CHANNELS, rate=FS,
                    input=True, frames_per_buffer=CHUNK)
'''

stream = audio.open(input_device_index=0,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=FS,
                    input=True,
                    frames_per_buffer=CHUNK
                    )

global keep_going

i = 0
f, ax = plt.subplots(2)

x = np.arange(10000)
y = np.random.randn(10000)
li, = ax[0].plot(x, y)
ax[0].set_xlim(0, 1000)
ax[0].set_ylim(-5000, 5000)
ax[0].set_title("Raw Audio Signal")

li2, = ax[1].plot(x, y)
ax[1].set_xlim(0, 5000)
ax[1].set_ylim(-100, 100)
ax[1].set_title("Fast Fourier Transform")

plt.pause(0.01)
plt.tight_layout()

frames = []
keep_going = True

'''
trumpet_params, trumpet_bytes = input_wave('wavs/Trumpet.wav')
punch_params,punch_bytes = input_wave('wavs/Punch.wav')
'''


def delay(audio_bytes, params, offset_ms):
    '''
    offset ms = miliseconds
    '''
    #calculate the number of bytes which correspodns to the offset in ms
    offset = params.sampwidth*offset_ms*int(params.framerate/100)
    #create some silence
    beggining = b'\0'*offset
    #remove space from the end
    end = audio_bytes[:-offset]
    #from audioop import add
    return add(audio_bytes, beggining+end, params.sampwidth)


def echo_effect(audioin, delay_sec, Fs):
    filt = np.zeros(int(delay_sec*Fs+1))
    filt[0] = 1
    filt[int(delay_sec*Fs)] = 0.7
    out = np.convolve(audioin, filt, 'same')
    return out



def plot_data(in_data):
    audio_data = np.frombuffer(in_data, dtype=np.int16)
    dfft = 10.*np.log10(abs(np.fft.rfft(audio_data)))
    li.set_xdata(np.arange(len(audio_data)))
    li.set_ydata(audio_data)
    li2.set_xdata(np.arange(len(dfft))*10.)
    li2.set_ydata(dfft)
    #tutaj mozna wkleic wykres z opoznieniem i bedzie fajnie wygladalo
    frames.extend(audio_data.tolist())
    plt.pause(0.01)
    if keep_going:
        return True
    else:
        return False


stream.start_stream()
print("\n+---------------------------------+")
print("| Press Ctrl+C to Break Recording |")
print("+---------------------------------+\n")
while keep_going:
    try:
        frame = stream.read(CHUNK, exception_on_overflow=False)

        #dac tutaj echo

        plot_data(frame)
    except KeyboardInterrupt:
        print("keyboardinterrupt")
        keep_going = False
    except:
        pass

stream.stop_stream()
stream.close()

audio.terminate()

'''
wf = wave.open("WAVE_OUTPUT_FILENAME", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(FS)
wf.writeframes(b''.join(frames))
wf.close()
'''
