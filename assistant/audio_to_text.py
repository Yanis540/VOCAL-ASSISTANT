import whisper 
import pyaudio 
import wave 
from typing import List
import os 
model = whisper.load_model("small")
# result = model.transcribe("./assistant/audio.mp3")
file_dir = "./assistant/temp.wave"
CHUNK = 1024 
FORMAT = pyaudio.paInt16 
CHANNELS = 1 
RATE = 44100 
SECONDS = 10 
def save_frames_temp_file(frames:List[bytes],p:pyaudio.PyAudio)->None: 
    try : 
        wave_file = wave.open(file_dir,"wb")
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(p.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()
        return 
    except Exception as e :  
        raise Exception("Error saving to temporary file")
def transcribe(stream:pyaudio.PyAudio.Stream,p:pyaudio.PyAudio)->dict[str, str | list]:
    """_summary_
    
    Args:
        stream (pyaudio.PyAudio.Stream): _description_
        p (pyaudio.PyAudio): _description_

    Returns:
        dict[str, str | list]: _description_
>>>        result["text"] or result["segments"] or result["language"]
    """
    frames = []
    for i in range(0,int(RATE/CHUNK * SECONDS)): 
        data = stream.read(CHUNK)
        frames.append(data)
    save_frames_temp_file(frames,p)
    result = model.transcribe(file_dir)
    return result


