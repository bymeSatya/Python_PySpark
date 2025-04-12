#import pyspark
import streamlit as st

number = st.slider("Pick a number", 0, 100)

date = st.date_input("Pick a date")
