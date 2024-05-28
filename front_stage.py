# front_stage.py
from visualization.shapes import Point, Line, Triangle, Square, Cube, Sphere, Pyramid, Circle
from visualization.coordinate_manager import CoordinateManager

def setup_stage(coord_manager):
    shapes = [
        Cube(color=(1.0, 0.0, 0.0), shape_id=1, coord_manager=coord_manager),
        Triangle(color=(0.0, 1.0, 0.0), shape_id=2, coord_manager=coord_manager),
        Circle(x=0.0, y=0.0, radius=1, color=(0.0, 0.0, 1.0), shape_id=3, coord_manager=coord_manager)
    ]

    coord_manager.update_position(1, (-2.0, 0.0, -10.0))
    coord_manager.update_position(2, (2.0, 0.0, -10.0))
    coord_manager.update_position(3, (0.0, 0.0, -5.0))

    return shapes
