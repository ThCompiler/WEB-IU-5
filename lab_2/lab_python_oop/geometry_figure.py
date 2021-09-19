from abc import ABCMeta, abstractmethod, abstractproperty
from lab_python_oop.color import Color


class IGeometryFigure():
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self._color = Color()
        
    def __init__(self, color : Color):
        self._color = color
        
    def __init__(self, red : int, green : int, blue : int):
        self._color = Color(red, green, blue)
        
    @abstractmethod
    def square():
        raise NotImplementedError()
    
    @property
    def color(self) -> Color:
        return self._color
    
    @color.setter
    def color(self, color : Color):
        self._color = color
        
    @color.setter
    def color(self, red : int, green : int, blue : int):
        self._color = Color(red, green, blue)
        
    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError()