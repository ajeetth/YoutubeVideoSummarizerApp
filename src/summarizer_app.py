import streamlit as st
from llm_utils import (extract_transcript, generate_summary, Prompt)

st.title("Welcome to YouTube video Summarizer App!")
st.subheader("powered by gemini-2.0")
youtube_link = st.text_input("Paste the YouTube video link here : ")

if youtube_link:
     video_id = youtube_link.split("=")[1]
     print(video_id)
     st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

st.session_state.youtube_link = youtube_link

if st.button('Get Summary'):
    transcript_text = extract_transcript(youtube_link)
    if transcript_text:
        st.session_state.summary = generate_summary(transcript_text, Prompt)
        st.markdown("Summary :")
        st.write(st.session_state.summary)

if st.button('clear screen'):
    st.session_state.summary = None
    st.session_state.youtube_link = ""