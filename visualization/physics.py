import numpy as np

class PhysicsObject:
    def __init__(self, shape):
        self.mass = None
        self.shape = shape
        self.velocity = np.random.uniform(-0.01, 0.01, size=3)



    def apply_force(self, force):
        self.acceleration += force / self.mass

    def update(self, dt):
        # self.velocity += self.acceleration * dt
        self.shape.coord_manager.positions[self.shape.shape_id] = (
            self.shape.coord_manager.positions[self.shape.shape_id] + self.velocity * dt
        )
        # Reset acceleration
        self.acceleration = np.array([0.0, 0.0, 0.0], dtype=np.float32)

