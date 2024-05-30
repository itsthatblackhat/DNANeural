import os
from neuron import Neuron

def setup_stage(coord_manager):
    base_path = os.path.dirname(os.path.abspath(__file__))
    motor_neuron_path = os.path.join(base_path, 'visualization', 'neuronsvgs', 'motorneuron.svg')
    nerve_cell_path = os.path.join(base_path, 'visualization', 'neuronsvgs', 'nerve-cell.svg')
    sensory_neuron_path = os.path.join(base_path, 'visualization', 'neuronsvgs', 'sensoryneuron.svg')
    synapse_path = os.path.join(base_path, 'visualization', 'neuronsvgs', 'synapse.svg')

    neurons = [
        Neuron((20.0, 0.0, 0.0), (1.0, 0.0, 0.0), 'motorneuron', coord_manager, motor_neuron_path),
        Neuron((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), 'motorneuron', coord_manager, motor_neuron_path),
        Neuron((-20.0, 0.0, 0.0), (0.0, 0.0, 1.0), 'sensoryneuron', coord_manager, sensory_neuron_path),
        Neuron((40.0, 0.0, 0.0), (1.0, 1.0, 0.0), 'synapse', coord_manager, synapse_path)
    ]

    return neurons, synapse_path
