import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Weather Forecast', layout='centered')

st.header('Weather Forecast for the Next Days')
place = st.text_input('Place')
days = st.slider(label='Forecast Days', label_visibility='visible',
                 min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox(label='Select data to view',
                      options=['Temperature', 'Sky Conditions'])

st.subheader(f"{option} for the next {days} days in {place}")

dates = ['1', '2', '3']
temperatures = [10, 11, 25]

figure = px.line(x=dates, y=temperatures, labels={"x": 'Date', "y": 'Temperature (C)'})
st.plotly_chart(figure)
