from abstract_component import Component


class Resistor(Component):
    """Класс резистора"""
    def __init__(
        self, name: str,
        resistance: float,
        node_1: int,
        node_2: int,
        branch: int
    ):
        super().__init__(name, node_1, node_2, branch)
        self.resistance = resistance

    def get_conductance(self, dt: float) -> float:
        return 1.0 / self.resistance

    def get_history_current(self, dt: float) -> float:
        return 0.0

    def update(self, voltage: float, current: float, dt: float):
        self.voltage = voltage
        self.current = current
