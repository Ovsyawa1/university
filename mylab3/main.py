import json
from pathlib import Path
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

from inductor import Inductor
from abstract_component import Component
from capasitor import Capacitor
from circuit_solver import CircuitSolver
from source_ac import VoltageSourceAC
from source_dc import VoltageSourceDC
from resistor import Resistor


# Функция для создания элементов
def create_component(data: Dict) -> Component:
    component_type = data['type']
    name = data['name']
    node_1 = data['node_1']
    node_2 = data['node_2']
    branch = data['branch']

    match component_type:
        case 'R':
            return Resistor(
                name, data['resistance'], node_1, node_2, branch
            )
        case 'L':
            return Inductor(
                name, data['inductance'], node_1, node_2, branch
            )
        case 'C':
            return Capacitor(
                name, data['capacitance'], node_1, node_2, branch
            )
        case 'E_DC':
            return VoltageSourceDC(
                name, data['voltage'], node_1, node_2, branch
            )
        case 'E_AC':
            return VoltageSourceAC(
                name,
                data['voltage'],
                data['frequency'],
                data['phase'],
                node_1,
                node_2,
                branch
            )
        case _:
            raise ValueError(f"Неизвестный тип компонента: {component_type}")


# Получение элементов цепи из JSON-файла
def load_circuit(filename: str) -> Tuple[Dict, List[Component], int]:
    with open(filename, 'r') as f:
        data = json.load(f)

    components = []  # массив из компонентов цепи
    nodes = set()  # множество для узлов
    branches = set()  # множество для веток
    elements_on_branch = {}

    # Создаем компоненты и собираем информацию об узлах
    for element in data['scheme_elements']:
        component = create_component(element)
        components.append(component)
        nodes.add(component.node_1)
        nodes.add(component.node_2)
        branches.add(component.branch)
        
        # Добавляем элемент в соответствующую ветвь
        if component.branch not in elements_on_branch:
            elements_on_branch[component.branch] = []
        elements_on_branch[component.branch].append(component)

    # print(f"Число узлов {len(nodes)}")
    # print(f"Число ветвей {len(branches)}")
    print(elements_on_branch)

    return (
        data['model_settings'],
        components,
        max(nodes) + 1,
        elements_on_branch,
        len(branches)
    )


# Моделировие переходного процесса и отображение графика
def simulate_circuit(filename: str) -> None:
    # Загружаем схему
    settings, components, nodes_count, elements_on_branch, branches_count = load_circuit(filename)
    solver = CircuitSolver(
        components,
        nodes_count,
        branches_count,
        elements_on_branch
    )

    # Параметры моделирования #
    # шаг на временность отрезке
    dt = settings['h']
    # время симуляции
    simulation_time = settings['simulation_time']
    # элемент, с которого производятся измерения
    monitor_component = settings['show_measurements_on']

    # Массивы для хранения результатов
    time_points = []  # временные точки для графика
    voltages = []  # значения напряжения для графика
    currents = []  # значения токов

    # Находим компонент для мониторинга
    monitor = None
    for comp in components:
        if comp.name == monitor_component:
            monitor = comp
            break

    if monitor is None:
        raise ValueError(f"Компонент {monitor_component} не найден в схеме")

    # Моделирование
    steps = int(simulation_time / dt)
    for _ in range(steps):
        solver.step(dt)
        time_points.append(solver.time)
        voltages.append(monitor.voltage)
        currents.append(monitor.current)

    # Построение графиков
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.plot(time_points, voltages)
    ax1.set_title(f'Напряжение на компоненте {monitor_component}')
    ax1.set_xlabel('Время, с')
    ax1.set_ylabel('Напряжение, В')
    ax1.grid(True)

    ax2.plot(time_points, currents)
    ax2.set_title(f'Ток через компонент {monitor_component}')
    ax2.set_xlabel('Время, с')
    ax2.set_ylabel('Ток, А')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

    # Вывод некоторых значений для проверки
    print(f"\nРезультаты моделирования для компонента {monitor_component}:")
    num_points = 5
    indices = [i * (len(time_points) - 1) // (num_points - 1) for i in range(num_points)]

    print("\nВремя (с) | Напряжение (В) | Ток (А)")
    print("-" * 40)
    for idx in indices:
        print(f"{time_points[idx]:8.3f} | {voltages[idx]:12.3f} | {currents[idx]:8.3f}")


def main():
    try:
        simulate_circuit(Path("mylab3", "rlc_circuit.json"))
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
