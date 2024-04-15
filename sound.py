import sounddevice
from scipy.io.wavfile import write

def save(sec):
    print("SPEAK NOW!!!")
    print("you can spesk for 15 sec")
    rece=sounddevice.rec((sec*44100),samplerate=44100,channels=2)
    sounddevice.wait()
    write("demo.wav",44100,rece)
    print("STOP! ")
    print("Your voice has been recorded")
save(15)
