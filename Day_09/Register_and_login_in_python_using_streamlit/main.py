import streamlit as st 
import hashlib 




if "users" not in st.session_state:
    st.session_state["users"] = {}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def home():
    st.title("simple login and registration system!")
    st.markdown("---")
    
    st.subheader("👋 Hello there!")
    st.write("This is a simple login and registration system built using Streamlit.")

    st.markdown("""
        ###  Features of This App:
        - 🔐 Secure password hashing
        - 📝 Simple and user-friendly registration
        - 🔓 Login functionality with feedback
        - 📦 Stored user data (in-session)
    """)

    st.image("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg", caption="Secure & Simple")

    st.info("Use the sidebar to Register or Login.")

    st.markdown("---")
    st.caption("Developed with ❤️ using Python & Streamlit")



def register():
    
    st.title("Register")
    username = st.text_input("Enter Username: ")
    password = st.text_input("Enter Password: ", type='password')

    if st.button("Register"):
        if not username or not password:
             st.warning("Username and Password cannot be empty.")
        elif username in st.session_state["users"]:
            st.warning("This username is already taken. Please choose another.")
        elif len(username) < 3:
            st.warning("Username must be at least 3 characters long.")
        elif len(password) < 6:
            st.warning("Password must be at least 6 characters long.")
        elif " " in username:
            st.warning("Username cannot contain spaces.")
        else:
            st.session_state["users"][username] = hash_password(password)
            st.success("You are registered successfully!")

def login():

    st.title("Login")

    if "login_username" not in st.session_state:
        st.session_state.login_username = ""
    if "login_password" not in st.session_state:
        st.session_state.login_password = ""

    username = st.text_input("Enter Username: ", key="login_username")
    password = st.text_input("Enter Password: ", type='password', key="login_password")


    if st.button("Login"):
        if username and password:
            hashed = hash_password(password)
            
            if st.session_state["users"].get(username) == hashed:
                st.success(f"Welcome back, {username}!")
            else:
                 st.warning("Username and Password cannot be empty.")


st.sidebar.title("🔄 Navigation")
choice = st.sidebar.selectbox("Choose an option", ["Home", "Register", "Login"])


if choice == "Home":
    home()
elif choice == "Register":
    register()
elif choice == "Login":
    login()
else:
    st.warning("Please choose an option")









