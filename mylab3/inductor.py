from abstract_component import Component


# Класс для моделирования индуктивности
class Inductor(Component):
    def __init__(
        self,  # экземпляр класса
        name: str,  # имя катушки
        inductance: float,  # индуктивность
        node_1: int,  # первый узел
        node_2: int,  # второй узел
        branch: int  # номер ветки
    ):
        super().__init__(name, node_1, node_2, branch)
        self.inductance = inductance
        self.prev_current = 0.0

    # Получение проводимости индуктивного элемента
    def get_conductance(self, dt: float) -> float:
        return dt / (2.0 * self.inductance)

    # Получение тока из предыдущей итерации
    def get_history_current(self, dt: float) -> float:
        return self.prev_current

    # Обновление параметров экземпляра класса
    def update(self, voltage: float, current: float, dt: float):
        self.voltage = voltage
        self.prev_current = self.current
        self.current = current
