import streamlit as st

from streamlit_geolocation import streamlit_geolocation

st.title("Streamlit Geolocation")

try:
    loc_string = streamlit_geolocation()
except:
    print("error")

if loc_string is not None:
    st.write(f"{loc_string}")