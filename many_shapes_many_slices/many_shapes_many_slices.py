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
    upper_left_corner = lower_left_corner + [0, 0, width]
    upper_right_corner = lower_left_corner + [0, width, width]
    lower_right_corner = lower_left_corner + [0, width, 0]

    return np.vstack((lower_left_corner, upper_left_corner, upper_right_corner, lower_right_corner))

# create random rectangles
n_shapes_per_slice = 100
n_slices = 5
n_shapes = n_shapes_per_slice * n_slices
slice_indices = np.expand_dims(np.repeat(np.arange(n_slices), n_shapes_per_slice), 1)

np.random.seed(0)
corners = 100 * np.random.random((n_shapes, 2))
corner_coords = np.hstack((slice_indices, corners))
widths = 15 * np.random.random((n_shapes,))
squares = [make_square(llc, w) for llc, w in zip(corner_coords, widths)]

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

