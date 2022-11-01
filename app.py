import streamlit as st
import pandas as pd
from datetime import date

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

today = date.today()

st.title('Image generator with Stable Diffusion')
st.header('text-to-image AI model')
st.subheader('Today is: {}'.format(today))

objects = st.text_input('Object(s) on the scene','A bear and a rooster')
background = st.text_input('Background of the scene','in a cyberpunk destroyed city')
st.write('Your input: ', objects, background)
st.dataframe(df)