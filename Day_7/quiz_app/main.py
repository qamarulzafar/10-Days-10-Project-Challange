import streamlit as st

# --- Custom CSS for Better Styling ---
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
        }
        .main {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2C3E50;
        }
        .question-box {
            background-color: #ECF0F1;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .stRadio > div {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .stButton > button {
            background-color: #3498DB;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #2980B9;
        }
        .score-box {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #27AE60;
            padding: 20px;
            background-color: #D4EFDF;
            border-radius: 10px;
        }
        .error-box {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #C0392B;
            padding: 10px;
            background-color: #FADBD8;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">🧠 Quiz Application</h1>', unsafe_allow_html=True)

# --- Questions Data ---
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

# --- Session State Initialization ---
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0

# --- If Quiz Completed ---
if st.session_state.question_index >= len(questions):
    st.markdown('<div class="score-box">🎉 Quiz Completed!</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="score-box">Your Score: {st.session_state.score} / {len(questions)}</div>', unsafe_allow_html=True)

    if st.button("Restart Quiz"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.rerun()

else:
    # --- Show Question & Progress ---
    current_question = questions[st.session_state.question_index]

    st.markdown(f'<div class="question-box"><b>Question {st.session_state.question_index + 1} of {len(questions)}</b></div>', unsafe_allow_html=True)
    st.subheader(current_question["Question"])

    # --- Radio Button for Options ---
    selected_option = st.radio("Choose your answer:", current_question["options"])

    # --- Submit Button ---
    if st.button("Submit Answer"):
        if selected_option == current_question["answer"]:
            st.markdown('<div class="score-box">✅ Correct! 🎉</div>', unsafe_allow_html=True)
            st.session_state.score += 1
        else:
            st.markdown(f'<div class="error-box">❌ Incorrect! The correct answer is **{current_question["answer"]}**.</div>', unsafe_allow_html=True)

        st.session_state.question_index += 1
        st.rerun()
