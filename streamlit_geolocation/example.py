import streamlit as st

from streamlit_geolocation import streamlit_geolocation

st.title("Streamlit Geolocation")

st.write("This is a demo of the Streamlit Geolocation component.")

st.write("The component is defined in `frontend/src/Geolocation.tsx`.")

st.write("The component is used in `example.py`.")

st.write("The component is published to PyPI as `streamlit_geolocation`.")

try:
    loc_string = streamlit_geolocation()
except:
    print("error")

if loc_string is not None:
    st.write(f"{loc_string}")