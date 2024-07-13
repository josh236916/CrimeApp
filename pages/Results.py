import streamlit as st
import os.path


my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Dependencies")

# Add a title to your app
st.title("Results For Classification and Regression")

image_options = {
    "Classification": path + "/image9.jpg",
    "Regression": path + "/image10.jpg",
   
}


selected_image = st.selectbox("Select an image:", list(image_options.keys()))

st.image(image_options[selected_image], caption=selected_image, use_column_width=True)