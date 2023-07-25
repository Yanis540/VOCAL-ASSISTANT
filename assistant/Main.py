import speech_recognition as sr
from audio_to_LLM_text import ask,write_terminal_without_space
import warnings
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
                audio_data = recognizer.listen(source)
                detected_audio_text = str(recognizer.recognize_whisper(audio_data,model="small"))
                if detected_audio_text is None or detected_audio_text.strip() =="": 
                    print()
                    continue 
                write_terminal_without_space(f"{detected_audio_text}")
                print()
                #! LLM 
                #! Text -> Audio : Not Working  
                ask(question=detected_audio_text,selected="Streaming",is_terminal=True)
            except Exception as e: 
                print(str(e))
                print("Unrocognized voice ")
                print()

listen()