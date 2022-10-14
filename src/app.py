import streamlit as st

# %%
from openpiv.piv import simple_piv
from openpiv import tools
import numpy as np
import imageio
import matplotlib.pyplot as plt

user_gifurl = 'https://github.com/alexlib/openpiv-app/raw/master/demo/ezgif.gif'
urls = {
    'Birds 1':'https://64.media.tumblr.com/3decdb9824c82cc625396d5162b9c72c/tumblr_ohqkj1wMvh1qckzoqo2_500.gifv',
    'Birds 2':'https://64.media.tumblr.com/15d6395f97f2d12e32a764c4a17be406/699471e89e1d5634-11/s500x750/eabb9c7c1ea719d4b9889d8e0217a878ed3f7a3f.gifv',
    'PIV Standard Project':'http://www.vsj.jp/~pivstd/gif/image04.gif',
    'Sneezing':'https://www.npr.org/assets/img/2016/08/23/sneeze-slomo.gif',
    'Rankine vortex':'https://github.com/ElsevierSoftwareX/SOFTX_2020_33/raw/master/images/rankine_vortex07_0.gif',
    'Uniform+Vortex': 'https://github.com/ElsevierSoftwareX/SOFTX_2020_33/raw/master/images/rk_uniform07_0.gif',
    'Stagnation flow':'https://github.com/ElsevierSoftwareX/SOFTX_2020_33/raw/master/images/stagnation07_0.gif',
    'Uniform flow':'https://github.com/ElsevierSoftwareX/SOFTX_2020_33/raw/master/images/uniform07_0.gif',
    'Parabolic profile':'https://github.com/ElsevierSoftwareX/SOFTX_2020_33/raw/master/images/parabolic07_0.gif',
    'Suction feeding fish':'https://i.makeagif.com/media/7-16-2015/7YeY1n.gif',
    'River (JPIV)':'https://eguvep.github.io/jpiv/fig/bode.gif',
    'User input': user_gifurl,
}

st.sidebar.markdown("## Select GIF")
# st.sidebar.markdown("You can **select** the values to change the *chart*.")

# Using object notation
with st.sidebar:
    choice = st.selectbox(
        "Select User input to paste your link:",
        urls.keys(),
    )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

st.title("OpenPIV analysis of GIFs")

st.markdown('## Selected:')
st.write(choice)

if choice == 'User input':
    gifurl = st.text_input('Paster here a link to GIF file:', value = user_gifurl)
else:
    gifurl = urls[choice]

# im = imageio.imread(imageio.core.urlopen(gifurl).read(), '.gif')
im = imageio.get_reader(gifurl)
st.image(gifurl)

images = []
for frame in im:
    # st.write(frame.shape)
    if frame.ndim > 2:
        frame = tools.rgb2gray(frame)
    images.append(frame)


frame_range = st.slider('Frames',value=(0,len(images)),min_value=0,max_value=len(images))
# st.write(frame_range[0],frame_range[1])

arrow_length = st.slider('Arrow length scaling',min_value=1,max_value=10,value=10)


newgif = []


counter = frame_range[0]
for I,J in zip(images[frame_range[0]:frame_range[1]-1],images[frame_range[0]+1:frame_range[1]]):
    x,y,u,v = simple_piv(I,J,plot=False)
    fig, ax = plt.subplots()
    ax.text(20,20, str(counter), color='y')
    ax.imshow(I, cmap='gray', alpha=0.8, origin="upper")
    ax.quiver(x, y, u, -v, scale=10*arrow_length, color="r")
    ax.axis('off')
    fig.savefig('tmp.png')
    # st.pyplot(fig)
    counter += 1
    newgif.append(imageio.imread('tmp.png'))

imageio.mimsave('tmp.gif', newgif)

st.image('tmp.gif')

# img_file_buffer = st.file_uploader("Upload a pair of images", type=["png", "jpg", "jpeg","tif","bmp"])
# img_file_extension = st.text("Extension") # need here to allow user to select image extension
# window_size = st.slider(
#    "Interrogation Window Size", 8, 128, windef_settings.windowsizes[0], 8
# )
# confidence_threshold = st.slider(
#     "Confidence threshold", 0.0, 1.0, DEFAULT_CONFIDENCE_THRESHOLD, 0.05
# )
# confidence_threshold = st.slider(
#     "Confidence threshold", 0.0, 1.0, DEFAULT_CONFIDENCE_THRESHOLD, 0.05
# )
# confidence_threshold = st.slider(
#     "Confidence threshold", 0.0, 1.0, DEFAULT_CONFIDENCE_THRESHOLD, 0.05
# )

# if img_file_buffer is not None:
#     windef_settings.filepath_images = './demo'
#     windef_settings.frame_pattern_a = img_file_extension
#     windef_settings.frame_pattern_b = None

# else:
#     # Format and Image Sequence
#     windef_settings.filepath_images = './demo'
#     windef_settings.frame_pattern_a = 'demo_b.bmp'
#     windef_settings.frame_pattern_b = 'demo_c.bmp'
#     # demo_image = DEMO_IMAGE
#     # image = np.array(Image.open(demo_image))

# success = process_images()
# fig,ax = plot_result()
# image, labels = annotate_image(image, detections, confidence_threshold)

# st.image(
#     image, caption=f"Processed image", use_column_width=True,
# )

# st.write(labels)

# %%
