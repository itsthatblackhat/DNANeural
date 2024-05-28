import pyaudio
import numpy as np

class AudioListener:
    def __init__(self, rate=44100, chunk=1024):
        self.rate = rate
        self.chunk = chunk
        self.audio_interface = pyaudio.PyAudio()
        self.stream = self.audio_interface.open(format=pyaudio.paInt16, channels=1,
                                                rate=self.rate, input=True,
                                                frames_per_buffer=self.chunk)

    def get_audio_data(self):
        if self.stream is None:
            return np.zeros(self.chunk)
        data = np.frombuffer(self.stream.read(self.chunk), dtype=np.int16)
        return data

    def stop_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    def __del__(self):
        self.stop_stream()
        self.audio_interface.terminate()
