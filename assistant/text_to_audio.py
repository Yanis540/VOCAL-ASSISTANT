import os
import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import (write as write_wav, read as read_wav)
import torchaudio
from pydub import AudioSegment
from pydub.playback import play

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
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""



def text_to_audio(text_prompt:str) : 
    
    print("Generating Audio")
    audio_array = generate_audio(text_prompt)
    print("Audio Generated")
    print("Playing")
    write_wav("./assistant/audio.wav", SAMPLE_RATE, audio_array)
    print("Finished Playing")
    return audio_array
# text_to_audio(text_prompt)