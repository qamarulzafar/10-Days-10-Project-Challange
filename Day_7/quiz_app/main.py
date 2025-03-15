import streamlit as st
import random
import time

st.title("Quiz Application")

questions = [
    {
        "Question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "Question": "Which is the national language of Pakistan?",
        "options": ["Urdu", "Punjabi", "Sindhi", "Pashto"],
        "answer": "Urdu"
    },
    {
        "Question": "Who is known as the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Quaid-e-Azam", "Benazir Bhutto"],
        "answer": "Quaid-e-Azam"
    },
    {
        "Question": "Which is the national animal of Pakistan?",
        "options": ["Markhor", "Lion", "Tiger", "Elephant"],
        "answer": "Markhor"
    },
    {
        "Question": "What is the currency of Pakistan?",
        "options": ["Dollar", "Rupee", "Taka", "Dirham"],
        "answer": "Rupee"
    }
]

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

current_question = st.session_state.current_question  # Use a separate variable for clarity

st.subheader(current_question["Question"])

selected_option = st.radio("Choose your answer", current_question["options"])

if st.button("Submit Answer"):
    if selected_option == current_question["answer"]:
        st.success("Correct! 🎉")
    else:
        st.error(f"Incorrect! The correct answer is **{current_question['answer']}**.")


    time.sleep(3)
    # Select a new question after submission
    st.session_state.current_question = random.choice(questions)

    # Refresh the app to show the new question
    st.rerun()
