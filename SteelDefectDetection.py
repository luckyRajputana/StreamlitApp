import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os, urllib, cv2

# st.title('Steel Defect Detection')
# '''
# This app is to take the steel image and mark the defected patch on the image with defect type mentioned on it.

# '''
# # Add a selectbox to the sidebar:
# a = [i for i in range(500)]
# add_selectbox = st.sidebar.selectbox('Please select the image id from the dropdown to find the defect',a)

# if st.sidebar.button('Select'):
# 	st.write('Image selected')
def main():
    # Render the readme as markdown using st.markdown.
    readme_text = st.markdown(get_file_content_as_string("instructions.md"))

    # Download external dependencies.
    for filename in EXTERNAL_DEPENDENCIES.keys():
        download_file(filename)

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Show instructions", "Run the app", "Show the source code"])
    if app_mode == "Show instructions":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Show the source code":
        readme_text.empty()
        st.code(get_file_content_as_string("app.py"))
    elif app_mode == "Run the app":
        readme_text.empty()
        run_the_app()

# Download a single file and make its content available as a string.
@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = '/' +path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")        


if __name__ == "__main__":
    main()        