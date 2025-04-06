from abstract_component import Component
from source_dc import VoltageSourceDC
import numpy as np
from typing import List, Tuple
from source_ac import VoltageSourceAC


# Решатель смоделированной цепи
class CircuitSolver:
    def __init__(self, components: List[Component], nodes_count: int):
        self.components = components
        self.nodes_count = nodes_count
        self.time = 0.0
        self.branches_count = len(components)

        # Инициализация матриц
        # Матрица инцидентности
        self.A = np.zeros((self.nodes_count - 1, self.branches_count))
        # Матрица проводимостей
        self.Y = np.zeros((self.branches_count, self.branches_count))
        # Вектор источников тока
        self.J = np.zeros(self.branches_count)
        # Вектор источников напряжения
        self.E = np.zeros(self.branches_count)

        # Формируем матрицу инцидентности A
        for i, comp in enumerate(components):
            if comp.node_1 > 0:
                self.A[comp.node_1 - 1, i] = 1
            if comp.node_2 > 0:
                self.A[comp.node_2 - 1, i] = -1

    # Итерация метода Доммеля
    def step(self, dt: float) -> Tuple[np.ndarray, np.ndarray]:
        # Обновляем матрицы Y, J, E
        for i, comp in enumerate(self.components):
            self.Y[i, i] = comp.get_conductance(dt)
            self.J[i] = comp.get_history_current(dt)
            if isinstance(comp, (VoltageSourceDC, VoltageSourceAC)):
                if isinstance(comp, VoltageSourceDC):
                    self.E[i] = comp.source_voltage
                else:
                    self.E[i] = comp.voltage_amplitude * np.sin(
                        2 * np.pi * comp.frequency * self.time + comp.phase
                    )

        # Формируем матрицу AYAt и вектор -A(J + YE)
        AYAt = self.A @ self.Y @ self.A.T
        # .T - метод для транспонирования матрицы
        # @ - матричное умножение
        right_side = -self.A @ (self.J + self.Y @ self.E)

        # Решаем СЛАУ
        try:
            V = np.zeros(self.nodes_count)
            V[1:] = np.linalg.solve(AYAt, right_side)
        except np.linalg.LinAlgError:
            print("Ошибка решения системы уравнений:")
            print("Матрица AYAt:")
            print(AYAt)
            print("Вектор правой части:")
            print(right_side)
            raise Exception("Ошибка решения СЛАУ")

        # Находим токи в ветвях
        # Проводимость * (Соединения * Напряжение + ЭДС) + источник тока
        currents = self.Y @ (self.A.T @ V[1:] + self.E) + self.J

        # Обновляем состояния компонентов
        for i, comp in enumerate(self.components):
            v1 = V[comp.node_1] if comp.node_1 > 0 else 0
            v2 = V[comp.node_2] if comp.node_2 > 0 else 0
            voltage = v1 - v2
            comp.update(voltage, currents[i], dt)

        self.time += dt
        return V, currents