import streamlit as st
import seaborn as sns

def main():
    st.title("Iris")

    df = sns.load_dataset("iris")

    st.dataframe(df)

    st.success("I like turtles")

if __name__ == "__main__":
    main()
