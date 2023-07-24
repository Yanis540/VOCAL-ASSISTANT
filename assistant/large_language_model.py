import openai 
import os 
import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit_pills import pills
from dotenv import load_dotenv
from bark import SAMPLE_RATE

from text_to_audio import text_to_audio
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
vocal_assistant_name="Lisa"
PROMPT = f"""
    You Are a vocal assistant named {vocal_assistant_name}, 
    you will answer  be provided with brief statements. 
    If you don't understand simply ask to repeat the question. Answer only the last question.
"""
CURRENT_CHAT = []
CURRENT_CHAT.append( {
    "role": "system",
    "content": PROMPT
},)
 
st.subheader("AI Assistant : Streamlit + OpenAI: `stream` *argument*")

def ask_without_stream(box:DeltaGenerator,question:str)->str:
    global CURRENT_CHAT 
    CURRENT_CHAT.append({"role": "user","content": question},)
    response =  openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=CURRENT_CHAT, 
        temperature=0,
        max_tokens=256,         
    )
    # Listen to response
    answer = response["choices"][0]["message"]["content"]
    audio_array=text_to_audio(answer)
    st.audio(audio_array,sample_rate=SAMPLE_RATE)
    # Listen to response
    box.write(answer)
    return answer

def ask_stream(box:DeltaGenerator,question: str):
    report = []
    full_answer=''
    global CURRENT_CHAT
    CURRENT_CHAT.append({"role": "user","content": question if (question is not  None ) or (question!="") else "Hello" },)
    for response in openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=CURRENT_CHAT,
        temperature=0,
        max_tokens=256, 
        stream=True
        
    ): 
        if "content" not in response["choices"][0]["delta"]:
            continue
        answer = str(response["choices"][0]["delta"]["content"] )
        print(answer)
        if answer.strip() == "" : 
            continue
        report.append(answer)
        # Listen to audio
        audio_array=text_to_audio(answer)
        st.audio(audio_array,sample_rate=SAMPLE_RATE)
        # Display result to the box 
        full_answer = "".join(report).strip()
        full_answer = full_answer.replace("\n", "")
        box.markdown(f'*{full_answer}*') 
    
    return full_answer  

# ask_stream("")
 
def main():
    selected = pills("", ["NO Streaming", "Streaming"], ["🎈", "🌈"])
    user_input = st.text_input("You: ",placeholder = "Ask me anything ...", key="input")

    if st.button("Submit", type="primary"):
        st.markdown("----")
        res_box = st.empty()
        if selected == "Streaming":
            result = ask_stream(res_box,user_input)
        else:
            result = ask_without_stream(res_box,user_input)
            
            
    st.markdown("----")
main()        
# : RUN SERVER  : streamlit run d:\Yanis\Développement\Mobile\Practice\2-VOCAL-ASSITANT\assistant\large_language_model.py