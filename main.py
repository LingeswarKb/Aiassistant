import streamlit as st 
import google.generativeai as genai


genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your name is AI Pullingo , You should act reply with attitude , reply to this in short: "+txt)
    return response.text

st.title("Pullingo Bot")


command = st.chat_input("Unaku Inna Venum Vro?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi How are you?"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Im Lingeswar's AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"Im Lingeswar's AI assistant"})
    elif "machi" in command:
        with st.chat_message("BOT"):
            st.write("sollu mame")
            st.session_state.message.append({"role":"BOT","message":"sollu mame"})
    elif "what do you know" in command:
        with st.chat_message("BOT"):
            st.write("Enaku ellam theryum Unaku Inna Venum")
            st.session_state.message.append({"role":"BOT","message":"Enaku ellam theryum Unaku Inna Venum"})
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
