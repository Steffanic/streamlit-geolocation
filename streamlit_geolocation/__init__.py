import streamlit.components.v1 as components
import os
# 
# absolute_path = os.path.dirname(os.path.abspath(__file__))
# frontend_path = absolute_path
# 
# streamlit_geolocation = components.declare_component(
#     "streamlit_geolocation", path=frontend_path
# )
_RELEASE = True
if not _RELEASE:
    _streamlit_geolocation = components.declare_component(
        "streamlit_geolocation",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _streamlit_geolocation = components.declare_component("streamlit_geolocation", path=build_dir)

def streamlit_geolocation():
    loc_string= _streamlit_geolocation(key="loc", default={'latitude': None, 'longitude': None, 'altitude': None, 'accuracy': None, 'altitudeAccuracy': None, 'heading': None, 'speed': None})
    return loc_string

