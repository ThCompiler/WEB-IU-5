
class Processor:

    def __init__(self, id: int, name: str, frequency: int, memory_cash: int):
        self.id = id
        self.name = name
        self.frequency = frequency
        self.memory_cash = memory_cash

    def __str__(self):
        return "Processor with id: " + str(self.id) + "; name: " + self.name + "; frequancy: " + str(self.frequency) + "; memory_cash: " + str(self.memory_cash)
    
    def __repr__(self) -> str:
        return self.__str__()

    def values(self):
        return self.name, self.frequency, self.memory_cash

class PC:

    def __init__(self, id: int, name: str, price: int, proc_id: int):
        self.id = id
        self.name = name
        self.price = price
        self.proc_id = proc_id

    def __str__(self):
        return "PC with id: " + str(self.id) + "; name: " + self.name + "; price: " + str(self.price) + "; proc_id: " + str(self.proc_id)
    
    def __repr__(self) -> str:
        return self.__str__()

    def values(self):
        return self.name, self.price


class PC_Processor:
    def __init__(self, proc_id: int, pc_id: int):
        self.proc_id = proc_id
        self.pc_id = pc_id
        
    def __repr__(self) -> str:
        return self.__str__()
    
    def values(self):
        return self.proc_id, self.pc_id

