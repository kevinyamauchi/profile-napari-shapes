"""
Display one 4-D image layer using the add_image API
"""

import numpy as np
import napari

# create one random polygon per "plane"
planes = np.tile(np.arange(128).reshape((128, 1, 1)), (1, 5, 1))
np.random.seed(0)
corners = np.random.uniform(0, 128, size=(128, 5, 2))
shapes = np.concatenate((planes, corners), axis=2)

base_cols = ['red', 'green', 'blue', 'white', 'yellow', 'magenta', 'cyan']
colors = np.random.choice(base_cols, size=128)

with napari.gui_qt():
    viewer = napari.view_shapes(
        np.array(shapes),
        shape_type='polygon',
        face_color=colors,
        name='sliced',
    )
