# Debug test file
import streamlit as st
import requests

st.title("Debug Test")

# Test API directly
api_url = "http://localhost:8000/api"

if st.button("Test 3 Movies"):
    response = requests.get(f"{api_url}/movies/recommendations?genre=Action&count=3")
    st.write("Response:", response.json())
    st.write("Count returned:", len(response.json()["movies"]))

if st.button("Test 9 Movies"):  
    response = requests.get(f"{api_url}/movies/recommendations?genre=Action&count=9")
    st.write("Response:", response.json())
    st.write("Count returned:", len(response.json()["movies"]))

# Test buttons
movie_test = {"id": 1, "title": "Test Movie"}
if st.button("Test See Details Button", key="test_btn"):
    st.write("Button clicked!")
    st.write("Movie:", movie_test)
