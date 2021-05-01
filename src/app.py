import streamlit as st
import openpiv

# %%
from openpiv import windef
from openpiv import tools
import numpy as np

# from const import CLASSES, COLORS
from settings import windef_settings

@st.cache
def process_images():
    windef.piv(windef_settings)
    return True


# @st.cache
# def plot_result(
#     image, detections, confidence_threshold=DEFAULT_CONFIDENCE_THRESHOLD
# ):
#     # loop over the detections
#     (h, w) = image.shape[:2]
#     labels = []
#     for i in np.arange(0, detections.shape[2]):
#         confidence = detections[0, 0, i, 2]

#         if confidence > confidence_threshold:
#             # extract the index of the class label from the `detections`,
#             # then compute the (x, y)-coordinates of the bounding box for
#             # the object
#             idx = int(detections[0, 0, i, 1])
#             box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#             (startX, startY, endX, endY) = box.astype("int")

#             # display the prediction
#             label = f"{CLASSES[idx]}: {round(confidence * 100, 2)}%"
#             labels.append(label)
#             cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
#             y = startY - 15 if startY - 15 > 15 else startY + 15
#             cv2.putText(
#                 image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2
#             )
#     return image, labels


st.title("PIV with OpenPIV")
img_file_buffer = st.file_uploader("Upload a pair of images", type=["png", "jpg", "jpeg","tif","bmp"])
img_file_extension = st.text("Extension") # need here to allow user to select image extension
window_size = st.slider(
    "Interrogation Window Size", 8, 128, windef_settings.windowsizes[0], 8
)
# confidence_threshold = st.slider(
#     "Confidence threshold", 0.0, 1.0, DEFAULT_CONFIDENCE_THRESHOLD, 0.05
# )
# confidence_threshold = st.slider(
#     "Confidence threshold", 0.0, 1.0, DEFAULT_CONFIDENCE_THRESHOLD, 0.05
# )
# confidence_threshold = st.slider(
#     "Confidence threshold", 0.0, 1.0, DEFAULT_CONFIDENCE_THRESHOLD, 0.05
# )

if img_file_buffer is not None:
    windef_settings.filepath_images = './demo'
    windef_settings.frame_pattern_a = img_file_extension 
    windef_settings.frame_pattern_b = None

else:
    # Format and Image Sequence
    windef_settings.filepath_images = './demo'
    windef_settings.frame_pattern_a = 'demo_b.bmp' 
    windef_settings.frame_pattern_b = 'demo_c.bmp'
    # demo_image = DEMO_IMAGE
    # image = np.array(Image.open(demo_image))

success = process_images()
fig,ax = plot_result()
# image, labels = annotate_image(image, detections, confidence_threshold)

st.image(
    image, caption=f"Processed image", use_column_width=True,
)

st.write(labels)
