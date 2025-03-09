import streamlit as st 
import random
import time 
import requests

st.title('Money Making Machine')

def generate_money():
    return random.randint(1, 1000)


st.subheader("Instant Cash generator")
if st.button("Generate Money"):
    message = st.empty() 
    message.write("Counting your money...")  
    time.sleep(2)  
    message.empty()
    amount = generate_money()
    st.success(f'You made ${amount}') 


def fetch_side_hastle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200 :
              hustles = response.json()
              return hustles["side_hustle"]
        else:
            return("Freelansing ")
        

    except:
        return ("Something Went Wrong !")
    

st.subheader("side_hustle_ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hastle()
    st.success(idea)






def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200 :
              quotes = response.json()
              return quotes["money_quotes"]
        else:
            return("Mooney is the root of all evils ")
        

    except:
        return ("Something Went Wrong !")
    

st.subheader("Money Making Motivation")
if st.button("Get Inspired"):
    idea = fetch_money_quotes()
    st.success(idea)