from abstract_component import Component
from capasitor import Capacitor
from current_source import CurrentSource
from source_dc import VoltageSourceDC
from source_ac import VoltageSourceAC
from inductor import Inductor

import numpy as np
from typing import List, Tuple


# Решатель смоделированной цепи
class CircuitSolver:
    def __init__(
        self, components: List[Component],
        nodes_count: int,
        branches_count: int,
        elements_on_branch: dict,
    ):
        self.components = components
        self.nodes_count = nodes_count
        self.time = 0.0
        self.branches_count = branches_count
        self.elements_on_branch = elements_on_branch

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
        for comp in components:
            if comp.node_1 > 0:
                self.A[comp.node_1 - 1, comp.branch - 1] = 1
            if comp.node_2 > 0:
                self.A[comp.node_2 - 1, comp.branch - 1] = -1

        # for i, comp in enumerate(components):
        #     if comp.node_1 > 0:
        #         self.A[comp.node_1 - 1, i] = 1
        #     if comp.node_2 > 0:
        #         self.A[comp.node_2 - 1, i] = -1

    # Итерация метода Доммеля
    def step(self, dt: float) -> Tuple[np.ndarray, np.ndarray]:
        for comp in self.components:
            # Один элемент на ветку - это очень важно!!!
            self.Y[comp.branch - 1, comp.branch - 1] = comp.get_conductance(dt)
            if isinstance(comp, CurrentSource):
                self.J[comp.branch - 1] = comp.get_history_current(dt)

            if isinstance(comp, VoltageSourceDC):
                self.E[comp.branch - 1] = comp.source_voltage

            if isinstance(comp, VoltageSourceAC):
                self.E[comp.branch - 1] += comp.voltage_amplitude * np.sin(
                    2 * np.pi * comp.frequency * self.time + comp.phase
                )

            # if isinstance(comp, Capacitor):
            #     self.E[comp.branch - 1] += (
            #         dt / (2 * comp.capacitance) * comp.current + comp.voltage
            #     )
                
            # if isinstance(comp, Inductor):
            #     self.E[comp.branch - 1] += (
            #         dt / (2 * comp.inductance) * comp.current + comp.voltage
            #     )

    # def step(self, dt: float) -> Tuple[np.ndarray, np.ndarray]:
    #     for i, comp in enumerate(self.components):
    #         # Один элемент на ветку - это очень важно!!!
    #         self.Y[i, i] = comp.get_conductance(dt)
    #         self.J[i] = comp.get_history_current(dt)
    #         if isinstance(comp, VoltageSourceDC):
    #             self.E[i] = comp.source_voltage
    #         if isinstance(comp, VoltageSourceAC):
    #             self.E[i] = comp.voltage_amplitude * np.sin(
    #                 2 * np.pi * comp.frequency * self.time + comp.phase
    #             )
    #         if isinstance(comp, Capacitor):
    #             self.E[i] += dt/(2 * comp.capacitance) * comp.current + comp.voltage
                    
    #         if isinstance(comp, Capacitor)

        # Формируем матрицу AYAt и вектор -A(J + YE)
        AYAt = self.A @ self.Y @ self.A.T
        # .T - метод для транспонирования матрицы
        # @ - матричное умножение
        right_side = -self.A @ (self.J + self.Y @ self.E)

        # Решаем СЛАУ
        try:
            V = np.zeros(self.nodes_count)
            # скип узла 0 и обновление матрицы узловых потенциалов
            V[1:] = np.linalg.solve(AYAt, right_side)
        except np.linalg.LinAlgError:
            print("Ошибка решения системы уравнений:")
            print("Матрица AYAt:")
            print(AYAt)
            print("Вектор правой части:")
            print(right_side)
            raise Exception("Ошибка решения СЛАУ")

        # Находим токи в ветвях
        # Проводимость * (Соединения(транспорнированная) * Напряжение + ЭДС)
        # + источники тока
        currents = self.Y @ (self.A.T @ V[1:] + self.E) + self.J

        # Обновляем состояния компонентов
        for comp in self.components:
            v1 = V[comp.node_1] if comp.node_1 > 0 else 0
            v2 = V[comp.node_2] if comp.node_2 > 0 else 0
            voltage = v1 - v2
            comp.update(voltage, currents[comp.branch - 1], dt)
            
        # for i, comp in enumerate(self.components):
        #     v1 = V[comp.node_1] if comp.node_1 > 0 else 0
        #     v2 = V[comp.node_2] if comp.node_2 > 0 else 0
        #     voltage = v1 - v2
        #     comp.update(voltage, currents[i], dt)

        self.time += dt
        return V, currents
