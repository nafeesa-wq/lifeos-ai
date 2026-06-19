import streamlit as st

st.title("🚀 My AI Startup App")

st.write("This is your first working version 🎉")

st.header("Try it out")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}! Your app is working perfectly 👍")

task = st.text_area("What do you want help with?")

if task:
    st.info("Nice! Next we will turn this into your AI idea step by step 🚀")