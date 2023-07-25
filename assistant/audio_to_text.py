
from speech_recognition import Recognizer,Microphone
from typing import Optional
def audio_to_text(source:Microphone,recognizer:Recognizer,model:Optional[str]="small"):
    """_summary_

    Args:
        source (Microphone): _description_
        recognizer (Recognizer): _description_
        model (Optional[str], optional): _description_. Defaults to "small".
    """
    audio_data = recognizer.listen(source)
    detected_audio_text = str(recognizer.recognize_whisper(audio_data,model=model))
    return detected_audio_text