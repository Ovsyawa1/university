from abstract_class import PrimaryEquipment

import random as rnd

class Bus(PrimaryEquipment):
    def __init__(self, name, voltage, sections, breaker):
        self.__name = name
        self.__voltage = voltage
        self.__sections = sections
        self.__breaker = breaker
        
    def set_name(self, name):
        self.__name = name
        
    def set_voltage(self, voltage):
        self.__voltage = voltage
        
    def set_sections(self, sections):
        self.__sections = sections
        
    def set_breaker(self, breaker):
        self.__breaker = breaker
        
    def get_name(self):
        return self.__name
        
    def get_voltage(self):
        return self.__voltage
        
    def get_sections(self):
        return self.__sections
        
    def get_breaker(self):
        return self.__breaker
    
    def get_info(self):
        return f"Bus - {self.__name}"
    
class Line(PrimaryEquipment):
    def __init__(self, name, voltage, breaker):
        self.__name = name
        self.__voltage = voltage
        self.__breaker = breaker
        
    def set_name(self, name):
        self.__name = name
        
    def set_voltage(self, voltage):
        self.__voltage = voltage
        
    def set_breaker(self, breaker):
        self.__breaker = breaker
        
    def get_name(self):
        return self.__name
        
    def get_voltage(self):
        return self.__voltage
        
    def get_breaker(self):
        return self.__breaker
    
    def get_info(self):
        return f"Line - {self.__name}"
        
class Transformer(PrimaryEquipment):
    def __init__(self, name, high_voltage, low_voltage):
        self.__name = name
        self.__high_voltage = high_voltage
        self.__low_voltage = low_voltage
        
    def set_name(self, name):
        self.__name = name
        
    def set_high_voltage(self, high_voltage):
        self.__high_voltage = high_voltage
        
    def set_low_voltage(self, low_voltage):
        self.__low_voltage = low_voltage
        
    def get_name(self):
        return self.__name
        
    def get_high_voltage(self):
        return self.__high_voltage
        
    def get_low_voltage(self):
        return self.__low_voltage
    
    def get_info(self):
        return f"Transformer - {self.__name}"
    
class Breaker(PrimaryEquipment):
    def __init__(self, name):
        self.__name = name
        self.__state = True
        
    def set_name(self, name):
        self.__name = name
        
    def set_state(self, state):
        self.__state = state
        
    def get_name(self):
        return self.__name
        
    def get_state(self):
        return self.__state
        
    def disconnect(self):
        self.__state = False
