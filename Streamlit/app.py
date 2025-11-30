import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello Streamlit")
st.write("This is simple example of a Streamlit app.")
df=pd.DataFrame({
    'First Column': [1,2,3,4],
    'Second Column':[10,20,30,40],
   
})
st.write("Here is the dataframe:")
st.write(df)

# creating a line chart
chart_data=pd.DataFrame( np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(chart_data)