import imageio
import os

# Define the directory containing the PNG images
png_dir = 'path/to/png/directory'

# Get a list of all PNG files in the directory
png_files = [f for f in os.listdir(png_dir) if f.endswith('.png')]

# Create an empty list to store the image frames
frames = []

# Loop through each PNG file and add it to the list of frames
for png_file in png_files:
    img = imageio.imread(os.path.join(png_dir, png_file))
    frames.append(img)

# Write the frames to a GIF file
imageio.mimsave('output.gif', frames)