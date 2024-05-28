# front_stage.py
from visualization.shapes import Cube, Triangle, Circle  # Ensure this is correct if you still need these shapes
from visualization.coordinate_manager import CoordinateManager
from neuron import Neuron

def setup_stage(coord_manager):
    shapes = [
        Neuron((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), 'sphere', coord_manager),
        Neuron((1.0, 1.0, 1.0), (0.0, 1.0, 0.0), 'sphere', coord_manager),
        Neuron((-1.0, -1.0, -1.0), (0.0, 0.0, 1.0), 'sphere', coord_manager)
    ]

    coord_manager.update_position(1, (0.0, 0.0, 0.0))
    coord_manager.update_position(2, (1.0, 1.0, 1.0))
    coord_manager.update_position(3, (-1.0, -1.0, -1.0))

    return shapes
