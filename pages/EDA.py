import streamlit as st
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Dependencies")

# Add a title to your app
st.title("Image Display in Streamlit")

image_options = {
    "MSE for Best features": path + "/image1.jpg",
    "Map showing Violent Crime Per Pop": path + "/image2.jpg",
    "Histogram showing Violent Crimes Per Pop": path +"/image3.jpg",
    "Q-Q plot showing Violent Crimes Per Pop": path +"/image4.jpg",
    "States with highest Violent Crimes Per Pop":path + "/image5.jpg",
    "Communities with highest Violent Crimes Per Pop": path +"/image6.jpg",
    "Actual vs Real Values for best Feature": path +"/image7.jpg",
    "Residual vs Fitted Values for best Feature": path +"/image8.jpg",
}


selected_image = st.selectbox("Select an image:", list(image_options.keys()))

st.image(image_options[selected_image], caption=selected_image, use_column_width=True)