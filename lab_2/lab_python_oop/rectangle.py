from lab_python_oop.color import Color
from lab_python_oop.geometry_figure import IGeometryFigure


class Rectangle(IGeometryFigure):
    
    def __init__(self):
        super().__init__()
        self.height = 0
        self.width = 0
    
    def __init__(self, height : int, width : int):
        super().__init__()
        self.height = height
        self.width = width
        
    def __init__(self, height : int, width : int, color : Color):
        super().__init__(color)
        self.height = height
        self.width = width
        
    def __init__(self, height : int, width : int, red : int, green : int, blue : int):
        super().__init__(red, green, blue)
        self.height = height
        self.width = width
        
    def square(self):
        return self.height * self.width
    
    def __repr__(self) -> str:
        return 'прямоугольник цвета {}; размером {}x{}; площадью {}.'.format(
            self.color,
            self.height,
            self.width,
            self.square()
        )