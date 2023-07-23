
import pyaudio 
import os 
from .audio_to_text import (
    transcribe, FORMAT,CHANNELS,RATE,SECONDS,CHUNK,file_dir
)
def main(): 
    
    # we have to record our salves here 
    try:
        p  = pyaudio.PyAudio()
        stream = p.open(format =FORMAT , channels=CHANNELS , rate = RATE , 
            input=True , frames_per_buffer=CHUNK
        ) 
        print("Microphone opened ")
        while True :
            print(f"Starting for {SECONDS} seconds ")
            result = transcribe(stream,p)
            print(result["text"])
    except Exception as e :
        print("Error Occured " , str(e))
    finally : 
        if stream : 
            stream.stop_stream()
            stream.close()
        if p : 
            p.terminate()

        if os.path.exists(file_dir): 
            os.remove(file_dir)
        