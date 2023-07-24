import whisper 
import pyaudio 
import wave 
from typing import List
import os 
import speech_recognition as sr
 

recognizer = sr.Recognizer()

def listen(): 
    mic = sr.Microphone(device_index=2)
    with mic as source : 
        while True : 
            try:
                print("Recording Speech")
                audio_data = recognizer.listen(source)
                print("Detecting")
                result = str(recognizer.recognize_whisper(audio_data,model="small"))
                print("Finished Recognition")
                if result is None or result.strip() =="": 
                    continue 
                
                print(result)
                # else send question to CHATGPT and display the answer 
                
                # if there's a result send it
            except Exception as e: 
                print("Unrocognized voice ")

listen()
# print(sr.Microphone.list_microphone_names())