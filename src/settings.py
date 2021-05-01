from openpiv import windef

windef_settings = windef.Settings()


'Data related settings'
# Folder with the images to process
windef_settings.filepath_images = "./demo/"

# Folder for the outputs
windef_settings.save_path = './results/'

# Root name of the output Folder for Result Files
windef_settings.save_folder_suffix = 'test'

# Format and Image Sequence
windef_settings.frame_pattern_a = '*.bmp' # file_list[0]

# windef_settings.frame_pattern_b = file_list[1]
windef_settings.frame_pattern_b = None

# If you want only one pair
# windef_settings.frame_pattern_a = file_list[0]
# windef_settings.frame_pattern_b = file_list[1]

'Region of interest'
# (50,300,50,300) #Region of interest: (xmin,xmax,ymin,ymax) or 'full' for full image
windef_settings.ROI = 'full' # (0,300,0,1024) #'full'

'Image preprocessing'
# 'None' for no masking, 'edges' for edges masking, 'intensity' for intensity masking
# WARNING: This part is under development so better not to use MASKS
windef_settings.dynamic_masking_method = 'None'
windef_settings.dynamic_masking_threshold = 0.005
windef_settings.dynamic_masking_filter_size = 7

'Processing Parameters'
windef_settings.correlation_method='circular'  # 'circular' or 'linear'
windef_settings.iterations = 2  # select the number of PIV passes

# add the interroagtion window size for each pass. 
# For the moment, it should be a power of 2 
windef_settings.windowsizes = (64,32,16) # if longer than n iteration the rest is ignored

# The overlap of the interroagtion window for each pass.
windef_settings.overlap = (32,16,8) # This is 50% overlap
# Has to be a value with base two. In general window size/2 is a good choice.

# methode used for subpixel interpolation: 'gaussian','centroid','parabolic'
windef_settings.subpixel_method = 'gaussian'

# order of the image interpolation for the window deformation
windef_settings.interpolation_order = 3
windef_settings.scaling_factor = 1  # scaling factor pixel/meter
windef_settings.dt = 1  # time between to frames (in seconds)

# 'Signal to noise ratio options (only for the last pass)'
# It is possible to decide if the S/N should be computed (for the last pass) or not
windef_settings.extract_sig2noise = False  # 'True' or 'False' (only for the last pass)

# method used to calculate the signal to noise ratio 'peak2peak' or 'peak2mean'
windef_settings.sig2noise_method = 'peak2peak'

# select the width of the masked to masked out pixels next to the main peak
windef_settings.sig2noise_mask = 1.2

# If extract_sig2noise==False the values in the signal to noise ratio
# output column are set to NaN

'vector validation options'

# choose if you want to do validation of the first pass: True or False
windef_settings.validation_first_pass = True
# only effecting the first pass of the interrogation the following passes
# in the multipass will be validated

'Validation Parameters'
# The validation is done at each iteration based on three filters.
# The first filter is based on the min/max ranges. Observe that these values are defined in
# terms of minimum and maximum displacement in pixel/frames.
windef_settings.MinMax_U_disp = (-50, 50)
windef_settings.MinMax_V_disp = (-50, 50)

# The second filter is based on the global STD threshold
windef_settings.std_threshold = 3  # threshold of the std validation

# The third filter is the median test (not normalized at the moment)
windef_settings.median_threshold = 3  # threshold of the median validation

# On the last iteration, an additional validation can be done based on the S/N.
windef_settings.median_size=1 #defines the size of the local median

'Validation based on the signal to noise ratio'
# Note: only available when extract_sig2noise==True and only for the last
# pass of the interrogation
# Enable the signal to noise ratio validation. Options: True or False
windef_settings.do_sig2noise_validation = True # This is time consuming

# minmum signal to noise ratio that is need for a valid vector
windef_settings.sig2noise_threshold = 2

'Outlier replacement or Smoothing options'

# Replacment options for vectors which are masked as invalid by the validation
windef_settings.replace_vectors = True # Enable the replacment. Chosse: True or False
windef_settings.smoothn=True #Enables smoothing of the displacemenet field
windef_settings.smoothn_p = 0.5 # This is a smoothing parameter

# select a method to replace the outliers: 'localmean', 'disk', 'distance'
windef_settings.filter_method = 'localmean'
# maximum iterations performed to replace the outliers
windef_settings.max_filter_iteration = 4
windef_settings.filter_kernel_size = 3  # kernel size for the localmean method

'Output options'
# Select if you want to save the plotted vectorfield: True or False
windef_settings.save_plot = False
# Choose wether you want to see the vectorfield or not :True or False
windef_settings.show_plot = False
windef_settings.scale_plot = 50  # select a value to scale the quiver plot of the vectorfield
# run the script with the given settings
