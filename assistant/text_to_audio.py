import os
from IPython.display import Audio
import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
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
print("Generating Audio")
audio_array = generate_audio(text_prompt)
print("Audio Generated")
print("Playing")
Audio(audio_array, rate=SAMPLE_RATE)
print("Finished Playinh")