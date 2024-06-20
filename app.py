import streamlit as st
from dotenv import load_dotenv
import os

def main():
    st.title("Environment variables")

    try:
        load_dotenv()
    except: pass

    at = os.environ["AIRTABLE_TOKEN"]
    ow = os.environ["OPENWEATHER_KEY"]

    st.success(at)
    st.success(ow)

if __name__ == "__main__":
    main()
