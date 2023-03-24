# Audio Recording
def AudioRecorder(secs):
    import pyaudio
    import wave
    # Set the audio parameters
    FORMAT = pyaudio.paInt16 
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = secs

    # Create a PyAudio object and open the microphone stream
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    # Create a list to store the recorded audio frames
    frames = []

    # Record audio from the microphone and store it in the frames list
    print('recording...')
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop the microphone stream and terminate the PyAudio object
    print('Recorded.')
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Create a new wave file from the recorded audio frames
    wf = wave.open("recorded_audio.wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

