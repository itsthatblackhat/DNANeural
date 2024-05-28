class Scene:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self, renderer):
        for obj in self.objects:
            obj.draw(renderer)
