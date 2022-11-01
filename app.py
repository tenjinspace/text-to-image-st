import streamlit as st
import pandas as pd
from datetime import date

today = date.today()

st.title('Image generator with Stable Diffusion')
st.header('text-to-image AI model')
st.subheader('Today is: {}'.format(today))

objects = st.text_input('Object(s) on the scene', 'a bear and a rooster')
background = st.text_input('Background of the scene', 'in a cyberpunk destroyed city')
query = objects + ' ' + background
st.write('Your input: ', query)

image = ''

st.image(image, caption=)