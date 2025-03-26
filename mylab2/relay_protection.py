from abstract_class import PrimaryEquipment

import random as rnd


class RelayProtection(PrimaryEquipment):
    def __init__(self, name, settings):
        self.__name = name
        self.__settings = settings

    def set_name(self, name):
        self.__name = name

    def set_settings(self, settings):
        self.__settings = settings

    def get_name(self):
        return self.__name

    def get_settings(self):
        return self.__settings

    @staticmethod
    def activation(failure_probability, current, current_threshold):
        ratio = rnd.random()
        if (ratio > failure_probability) and (current > current_threshold):
            return "Protection succeed"

        return "Protection failed"

    def get_info(self):
        return f"Rele - {self.__name}"
