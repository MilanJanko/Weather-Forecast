import streamlit as st
import plotly.express as px
from functions import get_data

st.set_page_config(page_title='Weather Forecast', layout='centered')

st.header('Weather Forecast for the Next Days')
place = st.text_input('Place')
days = st.slider(label='Forecast Days', label_visibility='visible',
                 min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox(label='Select data to view',
                      options=['Temperature', 'Sky Conditions'])

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Adding Temperature or Sky Conditions data
    dates, data = get_data(place, days, option)

    # Creating temperature or sky condition plot based on option

    # Create Temperature Figure
    if option == 'Temperature':
        figure = px.line(x=dates, y=data, labels={"x": 'Date', "y": 'Temperature (C)'})
        st.plotly_chart(figure)

    # Render images on the browser
    if option == 'Sky Conditions':
        # Adding path to the image - Dictionary that represents values from data if option is Sky Conditions
        image_path = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        render_list = [image_path[value] for value in data]
        st.image(render_list, width=100)
