import streamlit as st 
import random 
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
        
    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))



st.title("Password Generator")

length = st.slider("Select Password Length", min_value = 6, max_value = 30, value = 10)

use_digits = st.checkbox('Include Digits')

use_special = st.checkbox('Include Special Charector')


if st.button("Generate Password"):
    password = generate_password(length , use_digits, use_special)
    st.write(f"Generated password `{password}` ")


