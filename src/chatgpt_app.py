import streamlit as st
from PIL import Image
import numpy as np
import openpiv.tools
import openpiv.pyprocess

# Set the maximum file size that can be uploaded
st.set_option('deprecation.showfileUploaderEncoding', False)
# st.set_option('max_upload_size', 1024 * 1024 * 100) # 100 MB

st.title("Image Comparison Tool")

# Allow the user to upload two images
uploaded_img1 = st.file_uploader("Upload the first image", type=["png", "jpg"])
uploaded_img2 = st.file_uploader("Upload the second image", type=["png", "jpg"])

if uploaded_img1 and uploaded_img2:
    # Load the images into numpy arrays
    img1 = np.array(Image.open(uploaded_img1))
    img2 = np.array(Image.open(uploaded_img2))

    # Show the images
    st.image([img1, img2], caption=["First Image", "Second Image"], width=400)

    # Perform the analysis using openpiv
    frame_a = openpiv.tools.imread(uploaded_img1)
    frame_b = openpiv.tools.imread(uploaded_img2)

    u, v, sig2noise = openpiv.pyprocess.extended_search_area_piv(frame_a, frame_b, window_size=24, overlap=12, dt=0.02, search_area_size=64, sig2noise_method='peak2peak')

    x, y = openpiv.pyprocess.get_coordinates(image_size=frame_a.shape, window_size=24, overlap=12)

    # Show the results
    st.text("Displacement vectors:")
    st.image(openpiv.tools.display_vector_field(x, y, u, v, scaling_factor=3, width=400))
