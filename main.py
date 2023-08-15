import pandas as pd
import streamlit as st

st.set_page_config(page_title='Weather Forecast', layout='centered')

st.header('Weather Forecast for the Next Days')
place = st.text_input('Place')
days = st.slider(label='Forecast Days', label_visibility='visible',
                 min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox(label='Select data to view',
                      options=['Temperature', 'Sky Conditions'])

st.subheader(f"{option} for the next {days} days in {place}")
