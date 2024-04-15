import streamlit as st
import requests

# Create a Streamlit app
st.title('Sentiment Analysis with Fine Tuned Model')
st.write('Enter some text ')

text_input = st.text_input('Enter text here')

if st.button('Submit'):
    # Make a POST request to the Flask API endpoint
    response = requests.post('http://localhost:5000/predict', json={'text': text_input})
    data = response.json()

    # Display the results
    st.write(f'Sentiment is {data["sentiment"]}')
    st.write(f'Score is {data["score"]}')
