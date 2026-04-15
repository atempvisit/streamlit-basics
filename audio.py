import streamlit as st

st.title("Input your files", anchor=False)
st.divider()

# from directory or URL
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", start_time=0, format="audio/mp3", autoplay=False, loop=False)


audio_files = st.file_uploader('Enter your audio files', type=['mp3', 'wav'], accept_multiple_files = True)

print(type(audio_files))

if audio_files:
    for per_audio in audio_files:
        st.audio(per_audio, start_time=0, format="audio/mp3", autoplay=False, loop=False)
