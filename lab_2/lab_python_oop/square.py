from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    
    def __init__(self):
        super().__init__()
    
    def __init__(self, line : int):
        super().__init__(line, line)
    
    def __init__(self, line : int, color : Color):
        super().__init__(line, line, color)
    
    def __init__(self, line : int, red : int, green : int, blue : int):
        super().__init__(line, line, red, green, blue)
        
    def __repr__(self) -> str:
        return 'квадрта цвета {}; со стороной {}; площадью {}.'.format(
            self.color,
            self.height,
            self.square()
        )