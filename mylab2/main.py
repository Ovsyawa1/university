from substaion import Bus, Transformer, Line
from relay_protection import RelayProtection
from short_circuit import ShortCircuit

import json
import logging
import random as rnd


# Настройка логирования
logging.basicConfig(
    filename='substation_events.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Загрузка конфигурации из JSON
with open('D:/Table/my_dir/e-12-21/mylab2/equipment.json', 'r') as file:
    config = json.load(file)

# Создание оборудования подстанции
hv_bus = Bus(
    config['buses'][0]['name'],
    config['buses'][0]['voltage'],
    config['buses'][0]['sections'],
    config['buses'][0]['main_breakers'],
    config['buses'][0]["backup_breakers"]
)

lv_bus = Bus(
    config['buses'][1]['name'],
    config['buses'][1]['voltage'],
    config['buses'][1]['sections'],
    config['buses'][1]['main_breakers'],
    config['buses'][1]["backup_breakers"]
)

transformer1 = Transformer(
    config['transformers'][0]['name'],
    config['transformers'][0]['high_voltage'],
    config['transformers'][0]['low_voltage'],
    config['transformers'][0]['main_breakers'],
    config['transformers'][0]["backup_breakers"]
)

transformer2 = Transformer(
    config['transformers'][1]['name'],
    config['transformers'][1]['high_voltage'],
    config['transformers'][1]['low_voltage'],
    config['transformers'][1]['main_breakers'],
    config['transformers'][1]["backup_breakers"]
)

# Создание линий высокого напряжения
hv_lines = [
    Line(
        line['name'],
        config['substaion']['high_voltage'],
        line['main_breakers'],
        line['backup_breakers'],
    )
    for line in config['lines']['high_voltage']
]

# Создание линий низкого напряжения
lv_lines = [
    Line(
        line['name'],
        config['substaion']['low_voltage'],
        line['main_breakers'],
        line['backup_breakers'],
    )
    for line in config['lines']['low_voltage']
]

# Создание защит
main_protection = RelayProtection(
    config['protections'][0]['name'],
    config['protections'][0]['settings'],
)

backup_protection = RelayProtection(
    config['protections'][1]['name'],
    config['protections'][1]['settings']
)

# Список оборудования для случайного выбора места КЗ
equipment_list = [hv_bus, lv_bus, transformer1, transformer2] + hv_lines + lv_lines

# Моделирование 10 итераций
i = 1

while i <= 10:
    logging.info(f"\nIteration {i}")
    
    # Случайный выбор оборудования для КЗ
    faulted_equipment = rnd.choice(equipment_list)
    faulted_side = None
    if faulted_equipment is hv_bus or faulted_equipment is lv_bus:
        faulted_side = rnd.choice(faulted_equipment.get_sections())
    voltage = faulted_equipment.get_voltage()

    # Создание КЗ
    fault = ShortCircuit(faulted_equipment, voltage)
    current = fault.get_current()
    if faulted_side:
        logging.info(
            f"Short circuit on {faulted_equipment.get_info()} on {faulted_side}"
        )
    else:
        logging.info(
            f"Short circuit on {faulted_equipment.get_info()}"
        )
    logging.info(fault.get_info())

    # Проверка КЗ на самоустранение
    if fault.self_elimination_probability():
        logging.info("Short circuit has been eliminated by itself")
        i += 1
        continue

    # Срабатывание защит
    main_result = RelayProtection.activation(
        main_protection.get_settings()["failure_probability"],
        current,
        main_protection.get_settings()["current_threshold"]
    )
    logging.info(f"Main protection: {main_result}")
    if main_result:
        pass

    if main_result == "Protection failed":
        backup_result = RelayProtection.activation(
            backup_protection.get_settings()["failure_probability"],
            current,
            backup_protection.get_settings()["current_threshold"]
        )
        logging.info(f"Backup protection: {backup_result}")

    i += 1

logging.info("Simulation completed")
