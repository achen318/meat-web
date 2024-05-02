import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import librosa
import librosa.display
from IPython.display import Audio, display
import warnings
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout
import pyaudio
import queue

warnings.filterwarnings('ignore')

# Function to preprocess input
def preprocess_input(data):
    # Convert to floating-point and normalize
    data_float = data.astype(np.float32) / np.iinfo(data.dtype).max
    # Extract MFCC features
    mfcc = np.mean(librosa.feature.mfcc(y=data_float, sr=44100, n_mfcc=40).T, axis=0)
    return np.expand_dims(mfcc, axis=0)


# Load the model
if os.path.exists("emotion_detection_model.h5"):
    model = load_model("emotion_detection_model.h5")

# Define emotion labels
emotion_labels = ['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']

# PyAudio parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Queue for audio data
audio_queue = queue.Queue()

# Audio callback function
def audio_callback(in_data, frame_count, time_info, status):
    audio_queue.put(in_data)
    return (None, pyaudio.paContinue)

# Create PyAudio object
p = pyaudio.PyAudio()

# Open microphone stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                stream_callback=audio_callback)

print("Listening...")

try:
    while True:
        # Get audio data from queue
        audio_data = audio_queue.get()
        # Convert bytes to numpy array
        audio_np = np.frombuffer(audio_data, dtype=np.int16)
        # Preprocess the input
        input_data = preprocess_input(audio_np)
        # Get model's prediction
        prediction = model.predict(input_data)
        # Get the predicted emotion label
        predicted_label = emotion_labels[np.argmax(prediction)]
        # Print the predicted emotion label
        print("Predicted emotion:", predicted_label)
except KeyboardInterrupt:
    print("Stopped by user")

# Close stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()
