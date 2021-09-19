
class Color:
    
    def __init__(self):
        self._R = 0
        self._G = 0
        self._B = 0
        
    def __init__(self, red : int, green : int, blue : int):
        self._R = red
        self._G = green
        self._B = blue
        
    @property
    def R(self) -> int:
        return self._R
    
    @R.setter
    def R(self, value : int):
        self._R = value
        
    @property
    def G(self) -> int:
        return self._G
    
    @G.setter
    def G(self, value : int):
        self._G = value
        
    @property
    def B(self) -> int:
        return self._B
    
    @B.setter
    def B(self, value : int):
        self._B = value
        
    def __repr__(self) -> str:
        return 'RGB ({} {} {})'.format(
            self.R,
            self.G,
            self.B
        )