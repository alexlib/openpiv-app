import streamlit as st

# %%
from openpiv import pyprocess, tools
import numpy as np
import imageio
import matplotlib.pyplot as plt

user_gifurl = 'https://github.com/alexlib/openpiv-app/raw/master/demo/ezgif.gif'
urls = {
    'Snow after turbine':'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM215bHk4ZmczbTd5eTZ2Ym9pNHR0dzV6bHQ3dXNpcjJ6bWkzNWc5ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m9wxuXGSbTwOasOedM/giphy.gif',
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
    vel = process.extended_search_area_piv(
        I.astype(np.int32), J.astype(np.int32), 
        window_size=32,
        search_area_size=64,
        overlap=8
    )
    x, y = pyprocess.get_coordinates(image_size=frame_a.shape,
                                     search_area_size=64, overlap=8)

    # fig, ax = plt.subplots(1, 2, figsize=(11, 8))
    # ax[0].imshow(frame_a, cmap=plt.get_cmap("gray"), alpha=0.8)
    # ax[0].quiver(x, y, vel[0], -vel[1], scale=50, color="r")
    # ax[1].quiver(x, y[::-1, :], vel[0], -1*vel[1], scale=50, color="b")
    # ax[1].set_aspect(1)
    # # ax[1].invert_yaxis()
    # plt.show()
    
    # x,y,u,v,s2n = simple_piv(I,J,plot=False)
    fig, ax = plt.subplots()
    ax.text(20,20, str(counter), color='y')
    ax.imshow(I, cmap='gray', alpha=0.8, origin="upper")
    ax.quiver(x, y, vel[0], -vel[1], scale=50, color="r")
    # ax.quiver(x, y, u, -v, scale=10*arrow_length, color="r")
    ax[1].set_aspect(1)
    ax.axis('off')
    fig.savefig('tmp.png')
    # st.pyplot(fig)
    counter += 1
    newgif.append(imageio.imread('tmp.png'))

imageio.mimsave('tmp.gif', newgif)

st.image('tmp.gif')

