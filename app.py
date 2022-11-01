import streamlit as st
from datetime import date

today = date.today()

def main():
    st.title("Image generator with Stable Diffusion")
    st.markdown("text-to-image AI model")

    today = date.today()
    st.header('Today is: {}'.format(today))

    objects = st.text_input('Object(s) on the scene', 'a bear and a rooster')
    background = st.text_input('Background of the scene', 'in a cyberpunk destroyed city')
    query = objects + ' ' + background

    st.write('Your input: ', query)

if __name__ == "__main__":
    main()