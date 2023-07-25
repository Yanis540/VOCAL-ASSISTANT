import speech_recognition as sr
from ask_LLM_text_to_Audio import ask,write_terminal_without_space
import warnings
from audio_to_text import audio_to_text
warnings.filterwarnings("ignore", message=".*The 'nopython' keyword.*")
recognizer = sr.Recognizer()

def listen(): 
    mic = sr.Microphone(device_index=0)
    with mic as source : 
        print("Lisa : Hello how can i help you ?")
        
        while True : 
            try:
                #! Audio -> Text 
                write_terminal_without_space("You : ")
                detected_audio_text = audio_to_text(source,recognizer)
                if detected_audio_text is None or detected_audio_text.strip() =="": 
                    print()
                    continue 
                write_terminal_without_space(f"{detected_audio_text}")
                print()
                #! LLM 
                #! Text -> Audio   
                ask(question=detected_audio_text,selected="Streaming",is_terminal=True)
            except Exception as e: 
                print(str(e))
                print("Unrocognized voice ")
                print()

listen()