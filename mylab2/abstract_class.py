from abc import ABC, abstractmethod

class PrimaryEquipment(ABC):
    def __init__(self, name, voltage):
        self.name = name
        self.voltage = voltage

    @abstractmethod
    def get_info(self):
        pass