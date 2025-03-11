from abstract_class import PrimaryEquipment

import random as rnd

class Bus(PrimaryEquipment):
    def __init__(self, name, voltage, sections, breaker):
        super().__init__(name, voltage)
        self.sections = sections
        self.breaker = breaker
        
    def get_info(self):
        return(f"Bus - {self.name}")
    
class Line(PrimaryEquipment):
    def __init__(self, name, voltage, breaker):
        super().__init__(name, voltage)
        self.breaker = breaker
        
    def get_info(self):
        return(f"Line - {self.name}")
    
class Transformer(PrimaryEquipment):
    def __init__(self, name, high_voltage, low_voltage):
        super().__init__(name, high_voltage)
        self.low_voltage = low_voltage
        
    def get_info(self):
        return(f"Transformer - {self.name}")
    
class Breaker(PrimaryEquipment):
    def __init__(self, name):
        self.name = name
        
    def disconnect():
        pass
