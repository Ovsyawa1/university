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
