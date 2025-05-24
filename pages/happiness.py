import streamlit as st
import pandas as pd
import plotly.express as px

def get_data(x_axis, y_axis):
    x_axis = x_axis.lower()
    y_axis = y_axis.lower()

    df = pd.read_csv("files/happy.csv")
    x_axis_list = df[x_axis].tolist()
    y_axis_list = df[y_axis].tolist()
    return x_axis_list, y_axis_list

st.title("In Search for Happiness")

x_axis_value = st.selectbox("Select data for X-axis", ("GDP", "Happiness", "Generosity"))
y_axis_value = st.selectbox("Select data for Y-axis", ("GDP", "Happiness", "Generosity"))


x_values, y_values = get_data(x_axis_value, y_axis_value)

st.subheader(f"{x_axis_value} and {y_axis_value}")

figure = px.scatter(x=x_values, y=y_values, labels={"x": x_axis_value, "y": y_axis_value})
st.plotly_chart(figure)