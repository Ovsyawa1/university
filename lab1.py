from math import sqrt
from statistics import median
from random import randint

## Задание №1 ##

# Инициализация переменных
i = 0
arr = []

# Логика программы
while (i <= 15):
    arr.append(i)
    i += 1
    
print(arr)


## Задание №2 ##

# Инициализация переменных
my_set = set()

# Логика программы
for element in arr:
    if element <= 10:
        my_set.add(element)
    else:
        break
    
print(my_set)


## Задание №3 ##

# Инициализация переменных
i = 0

# Логика программы
while i <= 11:
    arr.pop(0)
    i += 1
    
print(arr)

## Задание №4 ##

# Инициализация переменных
arr_copy = arr.copy()

# Логика программы
for i in range(len(arr_copy)):
    if arr_copy[i] < 50:
        arr_copy[i] *= 3
    else:
        arr_copy[i] += 39
        
my_map_object = map(lambda x: x, arr_copy) # создание объекта типа map
my_tuple = tuple(my_map_object) # превращение объекта типа map в кортеж (tuple)

print(my_tuple)

## Задание №5 ##

def find_circle_around_rectangle(lenghts: list, widths: list):
    if len(lenghts) != len(widths):
        raise Exception("You've inputed wrond data")
    n = len(lenghts) # предполагаю 
    circle_radiuses = []
    
    # Создание кортежа из радиусов кругов
    for i in range(n):
        circle_radius = sqrt(lenghts[i]^2 + widths[i]^2)/2
        circle_radiuses.append(circle_radius)
    
    circle_tuple_map = map(lambda x: x, circle_radiuses)
    circle_tuple = tuple(circle_tuple_map)
    
    # фильтрация
    radiuses_average = sum(circle_radiuses)/n
    radiuses_for_delete = []
    
    for i in range(len(circle_radiuses)):
        if circle_radiuses[i] > (radiuses_average * 1.1):
            radiuses_for_delete.append(circle_radiuses[i])
    
   
    circle_radiuses = list(filter(lambda x: x <= (radiuses_average * 1.1), circle_radiuses))
    
    # Объявление переменной для хранения перемноженных отфильтрованных значений
    radiuses_multiplication = 1
    
    for i in range(len(circle_radiuses)):
        radiuses_multiplication *= circle_radiuses[i]
        
    result = radiuses_multiplication/n # разделил перемножение на длину исходного массива 
    
    print(circle_radiuses)
    
    return result
    
lengths = [1, 2, 3, 4]
widths = [20, 3, 4, 5]

result = find_circle_around_rectangle(lenghts=lengths, widths=widths)
print(f"Function result = {result: .3f}")

## Задание №6 ##

def create_list(start: int, stop: int, step: int):
    my_arr = []
    k = 0 # итератор для количества чичел кратных 7
    for i in range(start, stop, step):
        my_arr.append(i)
        
    new_arr = list(filter(lambda x: x % 7 == 0, my_arr))
    
    arr_median = median(my_arr)
    my_result = k - arr_median
    
    if my_result < 0:
        new_arr.sort(reverse=True)
    elif my_result > 0:
        my_arr_copy = new_arr.copy()
        my_arr_copy.insert(0, my_result)
    else:
        print("The result equals zero!")

    return new_arr

result_arr = create_list(0, 100, 14)
print(result_arr)

## Задание №7 ##

def dice_game(players_count: int, players_names: list):
    players_score = []
    max_index = 0
    
    for i in range(players_count):
        dice_value = randint(1, 6)
        players_score.append(dice_value)
        print(
            f"Игрок: {players_names[i]} \nВыбросил: {players_score[i]}\n"
        )
    
    max_dice_value = max(players_score)
    print("Победители:")
    
    for i in range(len(players_score)):
        if players_score[i] == max_dice_value:
            print(f"{players_names[i]}")
    
    
        
dice_game(5, ["Artem", "Oleg", "Vova", "Andrew", "Kirill"])