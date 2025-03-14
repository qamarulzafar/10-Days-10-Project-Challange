import streamlit as st
import pandas as pd
import datetime
import os
import csv

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])  
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

data = load_mood_data()
if not data.empty:
    st.subheader("Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"]) #Consistent uppercase "Date"
    mood_count = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_count)