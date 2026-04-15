import streamlit as st

st.title("Input your files", anchor=False)
st.divider()

# from directory or URL
st.video("https://www.w3schools.com/html/mov_bbb.mp4", start_time=0, format="video/mp4", autoplay=False, loop=False)


video_files = st.file_uploader('Enter your video files', type=['mp4', 'avi'], accept_multiple_files = True)

print(type(video_files))

button = st.button("Submit")

if button:
    if video_files:
        for per_video in video_files:
            st.video(per_video, start_time=0, format="video/mp4", autoplay=False, loop=False)
        
        st.success("Your video files have been uploaded successfully!")

    else:
        st.warning("Please upload at least one video file before submitting.")
        # st.error("No video files uploaded. Please try again.")