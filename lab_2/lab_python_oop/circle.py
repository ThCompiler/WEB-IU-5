from lab_python_oop.color import Color
from lab_python_oop.geometry_figure import IGeometryFigure 

import math

class Circle(IGeometryFigure):
    def __init__(self):
        super().__init__()
        self.radius = 0
    
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def __init__(self, radius, color : Color):
        super().__init__(color)
        self.radius = radius
        
    def __init__(self, radius, red : int, green : int, blue : int):
        super().__init__(red, green, blue)
        self.radius = radius
        
    def square(self):
        return math.pi * (self.radius ^ 2)

    def __repr__(self) -> str:
        return 'круг цвета {}; радиусом {}; площадью {}.'.format(
            self.color,
            self.radius,
            self.square()
        )
