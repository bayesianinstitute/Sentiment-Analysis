import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()

SERVER_IP = f'http://{os.getenv("SERVER_IP")}:5000'
# Create a Streamlit app
st.title('Sentiment Analysis with Fine Tuned Model')
st.write('Enter some text ')

text_input = st.text_input('Enter text here')

if st.button('Submit'):
    # Make a POST request to the Flask API endpoint
    response = requests.post(f'{SERVER_IP}/predict', json={'text': text_input})
    data = response.json()

    # Display the results
    st.write(f'Sentiment is {data["sentiment"]}')
    st.write(f'Score is {data["score"]}')
