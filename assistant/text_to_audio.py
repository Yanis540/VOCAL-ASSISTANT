import os
import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import (write as write_wav, read as read_wav)
import torchaudio
from pydub import AudioSegment
from pydub.playback import play
import streamlit as st
import base64
from playsound import playsound
import os 
torchaudio.set_audio_backend("soundfile")
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"
os.environ["XDG_CACHE_HOME"] = os.path.join(os.getcwd(), "cache") #replace this by whatever you want the cache path to b

print("Loading Models ...")
# download and load all models
preload_models( 
    text_use_small=True,
    coarse_use_small=True,
    fine_use_small=True,
)

# generate audio from text
text_prompted = """
    Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
    But I also have other interests such as playing tic tac toe.
"""

def text_to_audio(text_prompt:str) : 
    if text_prompt.split()=="":
        return 
    file_path = "./assistant/audio.wav"
    print("Generating Audio")
    audio_array = generate_audio(f"YOUNG BLONDE WOMAN : {text_prompt}",silent=True)
    write_wav(file_path, SAMPLE_RATE, audio_array)
    playsound(file_path)
    if os.path.exists(file_path): 
        os.remove(file_path)
    return audio_array
# text_to_audio(text_prompted)
# play_audio()