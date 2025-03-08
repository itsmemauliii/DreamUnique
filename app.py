import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/itsmemauliii/DreamUnique/main/flightsdetails.csv"  
    df = pd.read_csv(url)
    return df

df = load_data()

# Title
st.title("🔎 The Disappearing Billionaire's Flight Logs")
st.subheader("Analyze private jet travel data to track missing billionaire")

# Show dataset sample
st.write("### Flight Data Sample")
st.dataframe(df.head())

# Top 10 Departure Cities
st.write("### Top 10 Departure Cities")
flight_counts = df["ORIGIN_AIRPORT"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=flight_counts.values, y=flight_counts.index, ax=ax)
ax.set_xlabel("Number of Flights")
st.pyplot(fig)

# Flight Path Map
st.write("### Flight Path Visualization")
st.map(df[["LATITUDE", "LONGITUDE"]].dropna())  # Assuming dataset has latitude & longitude columns

# Suspicious Flights (Long Flight Duration)
st.write("### Possible Suspicious Flights")
suspicious_flights = df[df["AIR_TIME"] > 300]  # Example: Flights longer than 5 hours
st.dataframe(suspicious_flights)
