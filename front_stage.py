# front_stage.py
from neuron import Neuron

def setup_stage(coord_manager):
    neurons = [
        Neuron((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), 'neuron', coord_manager, 'C:\\JarvisDNA\\DNANeural\\visualization\\neuronsvgs\\motorneuron.svg'),
        Neuron((1.0, 1.0, 1.0), (0.0, 1.0, 0.0), 'neuron', coord_manager, 'C:\\JarvisDNA\\DNANeural\\visualization\\neuronsvgs\\nerve-cell.svg'),
        Neuron((-1.0, -1.0, -1.0), (0.0, 0.0, 1.0), 'neuron', coord_manager, 'C:\\JarvisDNA\\DNANeural\\visualization\\neuronsvgs\\motorneuron.svg')
    ]
    return neurons
