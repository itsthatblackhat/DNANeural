import numpy as np


class CoordinateManager:
    def __init__(self):
        self.positions = {}
        self.rotations = {}
        self.scales = {}

    def update_position(self, shape_id, position):
        self.positions[shape_id] = position

    def update_rotation(self, shape_id, rotation):
        self.rotations[shape_id] = rotation

    def update_scale(self, shape_id, scale):
        self.scales[shape_id] = scale

    def get_transformation_matrix(self, shape_id):
        pos = self.positions.get(shape_id, (0.0, 0.0, 0.0))
        rot = self.rotations.get(shape_id, (0.0, 0.0, 0.0))
        scale = self.scales.get(shape_id, (1.0, 1.0, 1.0))

        translation_matrix = np.eye(4)
        translation_matrix[:3, 3] = pos

        cx, cy, cz = np.cos(rot)
        sx, sy, sz = np.sin(rot)

        rotation_x_matrix = np.array([
            [1, 0, 0, 0],
            [0, cx, -sx, 0],
            [0, sx, cx, 0],
            [0, 0, 0, 1]
        ])

        rotation_y_matrix = np.array([
            [cy, 0, sy, 0],
            [0, 1, 0, 0],
            [-sy, 0, cy, 0],
            [0, 0, 0, 1]
        ])

        rotation_z_matrix = np.array([
            [cz, -sz, 0, 0],
            [sz, cz, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        rotation_matrix = rotation_x_matrix @ rotation_y_matrix @ rotation_z_matrix

        scale_matrix = np.eye(4)
        scale_matrix[0, 0] = scale[0]
        scale_matrix[1, 1] = scale[1]
        scale_matrix[2, 2] = scale[2]

        transformation_matrix = translation_matrix @ rotation_matrix @ scale_matrix
        return transformation_matrix
