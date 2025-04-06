from abc import ABC, abstractmethod


# Создание абстрактного класса
class Component(ABC):
    def __init__(self, name: str, node_1: int, node_2: int, branch: int):
        self.name = name
        self.node_1 = node_1
        self.node_2 = node_2
        self.branch = branch
        self.current = 0.0
        self.voltage = 0.0

    # Метод для получсения проводимости элемента
    @abstractmethod
    def get_conductance(self, dt: float) -> float:
        pass

    # Метод для получения тока из предыдущей итерации метода
    @abstractmethod
    def get_history_current(self, dt: float) -> float:
        pass

    # Метод для обновления параметров экземпляра класса
    @abstractmethod
    def update(self, voltage: float, current: float, dt: float):
        pass
