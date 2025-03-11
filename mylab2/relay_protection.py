from abstract_class import PrimaryEquipment

import random as rnd


class RelayProtection(PrimaryEquipment):
    def __init__(self, name, voltage, settings):
        super().__init__(name, voltage)
        self.settings = settings
        
    def activation(failure_probability):
        ratio = rnd.random()
        if ratio > failure_probability:
            return("Protection succeed")
        
        return("Protection failed")

    def get_info(self):
        return(f"Rele - {self.name}")