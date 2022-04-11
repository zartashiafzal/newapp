#import libraries
import streamlit as st
import plotly.express as px
import pandas as pd
# Adding header or title 
st.title("Plotly-titanic data & streamlit Combined for App making")
# import dataset
df=px.data.tips()
st.write(df)
# st.write(df.head()) # To take only first rows
st.write(df.columns)   
# As we known df.columns will give namesof all columns and we are using st.write to add names on app

#summary stat
st.write(df.describe())

#Data mangement

day_option=df["day"].unique().tolist()
day= st.selectbox("Which day tips should we load? ", day_option, 0)  #0 for index
df=df[df["day"]==day]

#after that a dropdown list will be created on app which will allow user to select day and days are unique values\

#Plotting data
st.title("gender wise plot")
fig=px.scatter(df, x='total_bill', y='tip', size='total_bill', color='sex', hover_name='sex',
                log_x=True, size_max=55, range_x=[6,59], range_y=[0.5, 8.5])

st.write(fig)

# Plotting bar chart & Line chart
st.title("Bar chart")
st.bar_chart(df['tip'])
st.title("Line chart")
st.line_chart(df['total_bill'])
