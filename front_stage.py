import os
from neuron import Neuron
from visualization.grid_floor import GridFloor

def setup_stage(coord_manager):
    base_path = os.path.dirname(os.path.abspath(__file__))
    motor_neuron_path = os.path.join(base_path, 'visualization', 'neuronsvgs', 'motorneuron.svg')
    sensory_neuron_path = os.path.join(base_path, 'visualization', 'neuronsvgs', 'sensoryneuron.svg')
    synapse_path = os.path.join(base_path, 'visualization', 'neuronsvgs', 'synapse.svg')

    neurons = [
        Neuron((10.0, 0.0, 0.0), (1.0, 0.0, 0.0), 'motorneuron', coord_manager, motor_neuron_path),
        Neuron((-10.0, 0.0, 0.0), (0.0, 1.0, 0.0), 'motorneuron', coord_manager, motor_neuron_path),
        Neuron((0.0, 0.0, 0.0), (0.0, 0.0, 1.0), 'synapse', coord_manager, sensory_neuron_path)
    ]

    grid_floor = GridFloor(size=50, step=1)

    return neurons, grid_floor
