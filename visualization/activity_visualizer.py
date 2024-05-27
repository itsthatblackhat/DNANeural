class ActivityVisualizer:
    def __init__(self, scene, renderer):
        self.scene = scene
        self.renderer = renderer

    def render(self):
        self.renderer.render(self.scene)
        print("Rendered scene")
