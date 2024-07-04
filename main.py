import streamlit as st
import requests
import os

st.header("HEALTHY DESSERT SEARCH ASSISTANT")

text = st.text_area("Enter one or more ingredients:")

my_secret = os.environ['DIFY_APP_SECRET']


headers = {
    'Authorization': f'Bearer {my_secret}',
    'Content-Type': 'application/json'
}

data = {
    'inputs': {
        'text': text
    },
    "response_mode": "blocking",
    "user": "healthy"
}

if st.button('Query'):
    base_url = "https://api.dify.ai/v1"
    path = "/complete-messages"
    response = requests.post(base_url + path, json=data, headers=headers)

    if response.status_code == 200:
          st.success('Query submitted successfully')

    result = response.json()
    st.markdown('### Result of request:')
    st.markdown(result['response'])

    print(answer.content)