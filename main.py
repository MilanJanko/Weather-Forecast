import streamlit as st
import plotly.express as px
from functions import get_data
from datetime import datetime

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
    try:
        # Adding Temperature or Sky Conditions data
        dates, temp, sky = get_data(place, days, option)

        # Creating temperature or sky condition plot based on option

        # Create Temperature Figure
        if option == 'Temperature':
            # Add temperature according to Celsius values
            data = [value / 10 for value in temp]
            figure = px.line(x=dates, y=data, labels={"x": 'Date', "y": 'Temperature (C)'},
                             line_shape='spline', markers=True, template='plotly')
            figure.update_layout(xaxis=dict(tickformat="%a %H:%M"),
                                 yaxis=dict(title="Temperature (C)"))
            st.plotly_chart(figure)

        # Render images on the browser
        if option == 'Sky Conditions':
            # Adding path to the image - Dictionary that represents values from data if option is Sky Conditions
            image_path = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                          'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}

            # Convert string dates to datetime objects
            datetime_dates = [datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S') for date_str in dates]
            # Prepare temperature, sky and images for rendering
            temp = [round(value/10, 1) for value in temp]
            render_list = [(image_path[value_sky], date, value_temp)
                           for value_sky, date, value_temp in zip(sky, datetime_dates, temp)]

            # Display images and formatted dates in rows of 7
            cols_per_row = 7
            for i in range(0, len(render_list), cols_per_row):
                row_images = render_list[i:i + cols_per_row]

                # Create a new row of columns
                cols = st.columns(cols_per_row)
                for col, (image_path, date, temperature) in zip(cols, row_images):
                    col.write(date.strftime('%a- %H:%M'))
                    col.image(image_path, width=120)
                    col.write(f"Temperature {temperature} °C")
                    col.write(10*'\n')

    except KeyError:
        st.error('Please enter valid city name.', icon="🚨")
