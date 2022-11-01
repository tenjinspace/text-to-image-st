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
st.write('Your input: ', objects)
#background = st.text_input()
#colors = st.text_input()
#style = st.text_input()

st.dataframe(df)