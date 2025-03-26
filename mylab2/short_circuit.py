import random as rnd


class ShortCircuit:
    def __init__(self, equipment, voltage):
        self.__equipment = equipment
        self.__voltage = voltage
        self.__fault_type = self._set_fault_type()
        self.__current = self._set_current()
        self.__elimination_ratio = 0.3

    def _set_fault_type(self):
        FAULT_TYPES = [
            "Three Phases",
            "Single Phase",
            "Two Phases",
            "Phase-to-Phase",
            ]
        return rnd.choices(FAULT_TYPES, weights=[5, 75, 10, 10])[0]

    def _set_current(self):
        if self.__fault_type == "Three Phases":
            current = rnd.randint(10, 40)
        elif self.__fault_type == "Single Phase":
            current = rnd.randint(5, 20)
        elif self.__fault_type == "Two Phases":
            current = rnd.randint(8, 35)
        elif self.__fault_type == "Phase-to-Phase":
            current = rnd.randint(7, 30)

        if self.__voltage == "110 kV":
            current = round(current * 2 / 3, 2)

        return current

    def set_equipment(self, equipment):
        self.__equipment = equipment

    def set_voltage(self, voltage):
        self.__voltage = voltage

    def set_fault_type(self, fault_type):
        self.__fault_type = fault_type

    def set_elimination_ratio(self, ratio):
        self.__elimination_ratio = ratio

    def get_equipment(self):
        return self.__equipment

    def get_voltage(self):
        return self.__voltage

    def get_fault_type(self):
        return self.__fault_type

    def get_current(self):
        return self.__current

    def get_elimination_ratio(self):
        return self.__elimination_ratio

    def get_info(self):
        return f"Short circuit: Type - {self.__fault_type}; Current: {self.__current} kA"

    def self_elimination_probability(self):
        if rnd.random() < self.__elimination_ratio:
            return True
        return False
