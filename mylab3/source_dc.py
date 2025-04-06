from abstract_component import Component


class VoltageSourceDC(Component):
    """Класс источника постоянного напряжения"""
    def __init__(self, name: str, voltage: float, node_1: int, node_2: int, branch: int):
        super().__init__(name, node_1, node_2, branch)
        self.source_voltage = voltage

    def get_conductance(self, dt: float) -> float:
        return 1e6  # Большая проводимость для источника напряжения

    def get_history_current(self, dt: float) -> float:
        return self.source_voltage * self.get_conductance(dt)

    def update(self, voltage: float, current: float, dt: float):
        self.voltage = voltage
        self.current = current
