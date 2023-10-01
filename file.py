import streamlit as st
import pandas as pd

st.subheader('Uploading the CSV file')
df = st.file_uploader('Upload the CSV file:',type = ['csv','xlsx'])

st.subheader('Loading the CSV file')
df = pd.read_csv('Blackfriday_sales.csv.csv')
if df is not None:
 st.table(df.head())  

st.subheader('Dealing with images directly')
st.image(r'C:\Users\rbgir\OneDrive\Desktop\streamlit\tim-swaan-eOpewngf68w-unsplash.jpg')

st.subheader('Working with images')
image_file = st.file_uploader("Upload the image file :",type = ['png','jpeg'])
if image_file is not None:
    st.image(image_file)

st.subheader('Working with videos')
videos_file = st.file_uploader("Upload the video file :",type = ['mkv','mp4'])
if videos_file is not None:
    st.video(videos_file,start_time=5)


st.subheader('Working with audios')
audio_file = st.file_uploader("Upload the audio file :",type = ['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())

