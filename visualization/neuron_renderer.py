from visualization.shader_sphere import ShaderSphereRenderer
from visualization.shader_cube import ShaderCubeRenderer

class NeuronRenderer:
    def __init__(self):
        self.sphere_renderer = ShaderSphereRenderer()
        self.cube_renderer = ShaderCubeRenderer()

    def render(self, neuron_type):
        if neuron_type == 'sphere':
            self.sphere_renderer.render_sphere()
        elif neuron_type == 'cube':
            self.cube_renderer.render_cube()
