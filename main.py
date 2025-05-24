import streamlit as st

st.title("Weather Forecast for the next days")

place = st.text_input("Enter the location: ")

days = st.slider("Forecast Days", min_value=1, max_value=5, step=1, help="Select the number of forecast days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader("{} for the next {} days in {}".format(option, days, place))