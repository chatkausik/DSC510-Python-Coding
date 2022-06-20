import numpy as np
from PIL import Image

# Create 3d numpy arrays of zeroes (black pixels) with yellow pixels.
data = np.zeros([5,4,3])

data[:] = [255,255,0]

print(data)

img = Image.fromarray(data,'RGB')
img.save('canvas.png')


