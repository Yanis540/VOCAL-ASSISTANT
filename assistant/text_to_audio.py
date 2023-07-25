import os
import os
from bark import SAMPLE_RATE, generate_audio, preload_models , save_as_prompt
from scipy.io.wavfile import (write as write_wav, read as read_wav)
import torchaudio
from pydub import AudioSegment
from pydub.playback import play
import streamlit as st
import base64
from playsound import playsound
import os 
import tempfile
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

history_prompt_path = "./assistant/audio/history_prompt.npz"



def text_to_audio(text_prompt:str) : 
    if text_prompt.split()=="":
        return 
    # Create a temporary file for audio storage and delete right away 
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as temp_file:
        temp_file_path = temp_file.name
    audio_array = generate_audio(f"YOUNG BLONDE WOMAN : {text_prompt}",silent=True,history_prompt=history_prompt_path)
    write_wav(temp_file_path, SAMPLE_RATE, audio_array)
    playsound(temp_file_path)
    return audio_array

def generate_default_prompt(prompt:str) : 
    full_generation, audio_array = generate_audio(prompt, output_full=True)
    write_wav("./assistant/audio/history_prompt.wav", SAMPLE_RATE, audio_array)
    save_as_prompt(history_prompt_path, full_generation)
    
DEFAULT_VOICE_PROMPT ="""
    YOUNG BLONDE WOMAN LONG HAIR : Hello, my name is Lisa. And, uh — and I like pizza. [laughs] 
    But I also have other interests such as playing tic tac toe.
"""    
# generate_default_prompt(DEFAULT_VOICE_PROMPT)

text_prompted = """
    Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
    But I also have other interests such as playing tic tac toe.
"""
# text_to_audio(text_prompted)
# play_audio()
# generate audio from text