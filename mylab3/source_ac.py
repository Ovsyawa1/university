from abstract_component import Component


import numpy as np


# Класс источника переменного напряжения
class VoltageSourceAC(Component):
    def __init__(
        self,
        name: str,
        voltage: float,
        frequency: float,  # частота
        phase: float,
        node_1: int,
        node_2: int,
        branch: int
    ):
        super().__init__(name, node_1, node_2, branch)
        self.voltage_amplitude = voltage
        self.frequency = frequency
        self.phase = phase
        self.time = 0.0

    def get_conductance(self, dt: float) -> float:
        return 1e6  # Большая проводимость для источника напряжения

    def get_history_current(self, dt: float) -> float:
        voltage = self.voltage_amplitude * np.sin(2 * np.pi * self.frequency * self.time + self.phase)
        return voltage * self.get_conductance(dt)

    def update(self, voltage: float, current: float, dt: float):
        self.voltage = voltage
        self.current = current
        self.time += dt
