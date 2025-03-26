from abstract_class import PrimaryEquipment


class Bus(PrimaryEquipment):
    def __init__(self, name, voltage, sections, main_breakers, backup_breakers):
        super().__init__(name, voltage)
        self.__sections = sections
        self.__main_breakers = main_breakers
        self.__backup_breakers = backup_breakers

    def set_sections(self, sections):
        self.__sections = sections

    def set_main_breakers(self, main_breakers):
        self.__main_breakers = main_breakers

    def set_backup_breakers(self, backup_breakers):
        self.__backup_breakers = backup_breakers

    def get_sections(self):
        return self.__sections

    def get_main_breakers(self):
        return self.__main_breakers

    def get_backup_breakers(self):
        return self.__backup_breakers

    def get_info(self):
        return f"Bus - {self.get_name()}"


class Line(PrimaryEquipment):
    def __init__(self, name, voltage, main_breakers, backup_breakers):
        super().__init__(name, voltage)
        self.__main_breakers = main_breakers
        self.__backup_breakers = backup_breakers

    def set_breaker(self, breaker):
        self.__breaker = breaker

    def set_main_breakers(self, main_breakers):
        self.__main_breakers = main_breakers

    def set_backup_breakers(self, backup_breakers):
        self.__backup_breakers = backup_breakers

    def get_main_breakers(self):
        return self.__main_breakers

    def get_backup_breakers(self):
        return self.__backup_breakers

    def get_info(self):
        return f"Line - {self.get_name()}"


class Transformer(PrimaryEquipment):
    def __init__(self, name, high_voltage, low_voltage, main_breakers, backup_breakers):
        super().__init__(name, high_voltage)
        self.__low_voltage = low_voltage
        self.__main_breakers = main_breakers
        self.__backup_breakers = backup_breakers
        
    def set_low_voltage(self, low_voltage):
        self.__low_voltage = low_voltage
        
    def set_main_breakers(self, main_breakers):
        self.__main_breakers = main_breakers
        
    def set_backup_breakers(self, backup_breakers):
        self.__backup_breakers = backup_breakers
        
    def get_voltage(self):
        return self.__low_voltage
        
    def get_main_breakers(self):
        return self.__main_breakers
    
    def get_backup_breakers(self):
        return self.__backup_breakers
    
    def get_info(self):
        return f"Transformer - {self.get_name()}"

  
class Breaker(PrimaryEquipment):
    def __init__(self, name):
        super().__init__(name, None)  # У выключателя нет напряжения
        self.__state = True
        
    def set_state(self, state):
        self.__state = state
        
    def get_state(self):
        return self.__state
        
    def disconnect(self):
        self.__state = False
        
    def get_info(self):
        return f"Breaker - {self.get_name()}"
