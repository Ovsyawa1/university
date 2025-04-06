from abstract_component import Component


# Класс для моделирования конденсатора
class Capacitor(Component):
    def __init__(
        self,  # эксземпляр класса
        name: str,  # имя название конденсатора
        capacitance: float,  # емкость
        node_1: int,  # первый узел
        node_2: int,  # второй узел
        branch: int  # номер ветки
    ):
        # Наследование инициализации от родительского класса
        super().__init__(name, node_1, node_2, branch)
        # Инициализация новых параметров
        self.capacitance = capacitance
        self.prev_voltage = 0.0

    # Получение проводимости
    def get_conductance(self, dt: float) -> float:
        return 2.0 * self.capacitance / dt

    def get_history_current(self, dt: float) -> float:
        return -self.get_conductance(dt) * self.prev_voltage

    def update(self, voltage: float, current: float, dt: float):
        self.voltage = voltage
        self.prev_voltage = voltage
        self.current = current
