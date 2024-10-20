import streamlit as st
import json
import os

# Function to load API key from a JSON file
def load_api_key():
    if os.path.exists("api_key.json"):
        with open("api_key.json", "r") as file:
            data = json.load(file)
            return data.get("api_key", "")
    return ""

# Function to save API key to a JSON file
def save_api_key(api_key):
    with open("api_key.json", "w") as file:
        json.dump({"api_key": api_key}, file)

# Streamlit App
st.title("API Key Storage")

# Load the stored API key (if exists)
stored_api_key = load_api_key()

# Input field for API key (manual entry)
api_key = st.text_input("Enter your API key", value=stored_api_key, type="password")

# Save the API key if it has changed
if st.button("Save API Key"):
    save_api_key(api_key)
    st.success("API key saved successfully!")

# Show the stored API key (for demonstration, masked)
if api_key:
    st.write(f"Stored API key (masked): {'*' * len(api_key)}")