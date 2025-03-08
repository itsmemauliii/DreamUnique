import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/itsmemauliii/DreamUnique/main/flightsdetails.csv"  
    df = pd.read_csv(url)
    
    # Remove any extra spaces in column names
    df.columns = df.columns.str.strip()
    
    return df

df = load_data()

# Title
st.title("🔎 The Disappearing Billionaire's Flight Logs")
st.subheader("Analyze private jet travel data to track missing billionaire")

# Show dataset sample
st.write("### 📊 Flight Data Sample")
st.dataframe(df.head())

# Debug: Display column names
st.write("### 🏷 Column Names in Dataset")
st.write(df.columns)

# Check if "ORIGIN_AIRPORT" column exists
if "ORIGIN_AIRPORT" in df.columns:
    st.write("### ✈️ Top 10 Departure Cities")
    flight_counts = df["ORIGIN_AIRPORT"].value_counts().head(10)

    fig, ax = plt.subplots()
    sns.barplot(x=flight_counts.values, y=flight_counts.index, ax=ax)
    ax.set_xlabel("Number of Flights")
    ax.set_ylabel("Origin Airport")
    st.pyplot(fig)
else:
    st.error("❌ 'ORIGIN_AIRPORT' column not found! Check dataset.")

# Flight Path Map
if "LATITUDE" in df.columns and "LONGITUDE" in df.columns:
    st.write("### 🗺️ Flight Path Visualization")
    st.map(df[["LATITUDE", "LONGITUDE"]].dropna())
else:
    st.warning("⚠️ 'LATITUDE' and 'LONGITUDE' columns not found! Skipping flight map.")

# Suspicious Flights (Long Flight Duration)
if "AIR_TIME" in df.columns:
    st.write("### 🚨 Possible Suspicious Flights")
    suspicious_flights = df[df["AIR_TIME"] > 300]  # Flights longer than 5 hours
    st.dataframe(suspicious_flights)
else:
    st.warning("⚠️ 'AIR_TIME' column not found! Unable to analyze suspicious flights.")
