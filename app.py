import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(page_title="Billionaire's Flight Logs", page_icon="✈️", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/itsmemauliii/DreamUnique/main/flightsdetails.csv"  
    df = pd.read_csv(url)
    return df

df = load_data()

# Initialize session state for buttons
if "show_sample" not in st.session_state:
    st.session_state["show_sample"] = False
if "show_suspicious" not in st.session_state:
    st.session_state["show_suspicious"] = False
if "show_map" not in st.session_state:
    st.session_state["show_map"] = False

# Title and Description
st.title("🔎 The Disappearing Billionaire's Flight Logs")
st.subheader("Analyze private jet travel data to track the missing billionaire")
st.markdown("Explore flight patterns, suspicious activity, and travel trends.")

# Sidebar Overview
st.sidebar.header("🔍 Data Overview")
if st.sidebar.button("Show Column Names"):
    st.sidebar.write(df.columns.tolist())

# Button for showing dataset sample
if st.button("Show Flight Data Sample"):
    st.session_state["show_sample"] = not st.session_state["show_sample"]
if st.session_state["show_sample"]:
    st.write("### Flight Data Sample")
    st.dataframe(df.head())

# Top 10 Departure Cities
if "origin" in df.columns:
    st.write("## 📍 Top 10 Departure Cities")
    flight_counts = df["origin"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=flight_counts.values, y=flight_counts.index, ax=ax, palette="coolwarm")
    ax.set_xlabel("Number of Flights")
    ax.set_ylabel("Departure City")
    ax.set_title("Top 10 Departure Cities by Flight Count")
    st.pyplot(fig)
else:
    st.error("❌ 'origin' column not found! Check dataset.")

# Flight Duration Distribution
if "air_time" in df.columns:
    st.write("## ⏳ Flight Duration Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["air_time"].dropna(), bins=30, kde=True, color="royalblue")
    ax.set_xlabel("Flight Duration (minutes)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Flight Durations")
    st.pyplot(fig)
else:
    st.warning("⚠️ 'air_time' column not found! Skipping flight duration analysis.")

# Button for suspicious flights
if "air_time" in df.columns:
    st.write("## 🚨 Possible Suspicious Flights")
    if st.button("Find Suspicious Flights (Air Time > 300 min)"):
        st.session_state["show_suspicious"] = not st.session_state["show_suspicious"]
    if st.session_state["show_suspicious"]:
        suspicious_flights = df[df["air_time"] > 300]
        st.dataframe(suspicious_flights)
else:
    st.warning("⚠️ 'air_time' column not found! Unable to analyze suspicious flights.")

# Footer
st.markdown("---")
st.markdown("🚀 **Created by Mauli Patel | Data Science & AI Enthusiast**")
