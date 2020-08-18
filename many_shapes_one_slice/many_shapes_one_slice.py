"""
Display one 4-D image layer using the add_image API
"""

import numpy as np
import napari
from skimage import data

# make 3D image
blobs = data.binary_blobs(
    length=128, blob_size_fraction=0.05, n_dim=3, volume_fraction=0.1
).astype(float)


def make_square(lower_left_corner, width):
    upper_left_corner = lower_left_corner + [0, width]
    upper_right_corner = lower_left_corner + [width, width]
    lower_right_corner = lower_left_corner + [width, 0]

    return np.vstack((lower_left_corner, upper_left_corner, upper_right_corner, lower_right_corner))

# create random rectangles
n_shapes = 1000
np.random.seed(0)
corners = 100 * np.random.random((n_shapes, 2))
widths = 15 * np.random.random((n_shapes,))
squares = [make_square(llc, w) for llc, w in zip(corners, widths)]

base_cols = ['red', 'green', 'blue', 'white', 'yellow', 'magenta', 'cyan']
colors = np.random.choice(base_cols, size=n_shapes)

with napari.gui_qt():

    viewer = napari.view_image(blobs)

    shapes_layer = viewer.add_shapes(
        squares,
        shape_type='rectangle',
        face_color=colors,
        name='sliced',
    )

