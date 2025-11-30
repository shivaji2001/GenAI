import streamlit as st
import pandas as pd
st.title("Hello Streamlit")
name=st.text_input("Enter your name:")
age=st.slider('Select your age:',0,100,25) #number between 0 and 100 with default 25
st.write(f"You are {age} years old.")
options=['Python','Java','C++','Javascript']
choice=st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected: {choice}")
if name:
    st.write(f"Hello, {name}!")

data={
    "Name":["Shivanshu","Alice","Bob"],
    "Age":[23,30,25],
    "City":["New York","Los Angeles","Chicago"]
}
df=pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
st.write(df)


uploaded_file=st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write("Here is the content of the uploaded file:")
    st.write(df)