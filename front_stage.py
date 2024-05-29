from neuron import Neuron
from visualization.coordinate_manager import CoordinateManager

def setup_stage(coord_manager):
    shapes = [
        Neuron((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), 'sphere', coord_manager),
        Neuron((1.0, 1.0, 1.0), (0.0, 1.0, 0.0), 'sphere', coord_manager),
        Neuron((-1.0, -1.0, -1.0), (0.0, 0.0, 1.0), 'sphere', coord_manager)
    ]

    coord_manager.update_position(id(shapes[0]), (0.0, 0.0, -10.0))
    coord_manager.update_position(id(shapes[1]), (2.0, 2.0, -10.0))
    coord_manager.update_position(id(shapes[2]), (-2.0, -2.0, -10.0))

    return shapes
