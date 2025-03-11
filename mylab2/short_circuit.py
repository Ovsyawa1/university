import random as rnd

class ShortCircuit:
    def __init__(self, equipment, voltage):
        self.equipment = equipment
        self.voltage = voltage
        self.fault_type = self._get_fault_type()
        
    def _get_fault_type(self):
        FAULT_TYPES = ["Three Phases", "Single Phase", "Two Phases", "Phase-to-Phase"]
        return(rnd.choices(FAULT_TYPES, weights=[5, 75, 10, 10])[0])
    
    def _get_current(self):
        self_elimination_ratio = 0.3
        if rnd.random() < self_elimination_ratio:
            return("Short circuit has been eliminated by itself")
        
        

    def get_info(self):
        return(f"Short circuit: Type = {self.fault_type}")
        
