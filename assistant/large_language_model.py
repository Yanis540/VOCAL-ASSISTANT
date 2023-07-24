import openai 
import os 
import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit_pills import pills
from dotenv import load_dotenv

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
    box.write(response["choices"][0]["message"]["content"])
    
    return response["choices"][0]["message"]["content"]

def ask_stream(box:DeltaGenerator,question: str):
    report = []
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
        report.append(response["choices"][0]["delta"]["content"])
        result = "".join(report).strip()
        result = result.replace("\n", "")
        # print(result)
        box.markdown(f'*{result}*') 
    
    return result 

# ask_stream("")
 
def main():
    selected = pills("", ["NO Streaming", "Streaming"], ["🎈", "🌈"])
    user_input = st.text_input("You: ",placeholder = "Ask me anything ...", key="input")

    if st.button("Submit", type="primary"):
        st.markdown("----")
        res_box = st.empty()
        if selected == "Streaming":
            ask_stream(res_box,user_input)
        else:
            ask_without_stream(res_box,user_input)
            
    st.markdown("----")
        
# : RUN SERVER  : streamlit run d:\Yanis\Développement\Mobile\Practice\2-VOCAL-ASSITANT\assistant\large_language_model.py