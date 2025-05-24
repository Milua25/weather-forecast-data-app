import streamlit as st
import plotly.express as px
from backend import *

st.title("Weather Forecast for the next days")

place = st.text_input("Enter the location: ")

days = st.slider("Forecast Days", min_value=1, max_value=5, step=1, help="Select the number of forecast days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader("{} for the next {} days in {}".format(option, days, place))

if place:
    filtered_data = get_weather_data(place,  days)

# dates = ["2022-02-25", "2022-02-26", "2022-02-27"]
# temp_list = [34, 76, 20]
# temperatures = [ days * i for i in temp_list]
    if filtered_data is None:
        st.info("Location does not exist!", icon="🚨")
    else:
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {
                "Clear" : "files/images/clear.png",
                "Clouds" : "files/images/cloud.png",
                "Rain" : "files/images/rain.png",
                "Snow" : "files/images/snow.png",
            }
            image_paths = [ images[condition]  for condition in filtered_data]
            print(image_paths)
            st.image(image_paths, width=150)


