from abstract_component import Component


class CurrentSource(Component):
    """Класс источника постоянного напряжения"""
    def __init__(self, name: str, node_1: int, node_2: int, branch: int, current: float):
        super().__init__(name, node_1, node_2, branch)
        self.source_current = current

    def get_conductance(self, dt: float) -> float:
        return 1e-6  # Маленькая проводимость для источника напряжения

    def get_history_current(self, dt: float) -> float:
        return self.source_current

    def update(self, voltage: float, current: float, dt: float):
        self.voltage = voltage
        self.current = current
