from abstract_class import PrimaryEquipment

import random as rnd


class RelayProtection(PrimaryEquipment):
    def __init__(self, name, voltage, settings):
        self.__name = name
        self.__voltage = voltage
        self.__settings = settings
        
    def set_name(self, name):
        self.__name = name
        
    def set_voltage(self, voltage):
        self.__voltage = voltage
        
    def set_settings(self, settings):
        self.__settings = settings
        
    def get_name(self):
        return self.__name
        
    def get_voltage(self):
        return self.__voltage
        
    def get_settings(self):
        return self.__settings
        
    @staticmethod
    def activation(failure_probability):
        ratio = rnd.random()
        if ratio > failure_probability:
            return "Protection succeed"
        
        return "Protection failed"

    def get_info(self):
        return f"Rele - {self.__name}"
