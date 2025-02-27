## Задание №5 ##

from math import sqrt
from turtle import width


def find_circle_around_rectangle(lenghts: list, widths: list):
    if len(lenghts) != len(widths):
        raise Exception("You've inputed wrond data")
    
    n = len(lenghts)
    circle_radiuses = []
    
    # Создание кортежа из радиусов кругов
    for i in range(n):
        circle_radius = sqrt(lenghts[i]^2 + widths[i]^2)/2
        circle_radiuses.append(circle_radius)
    
    circle_tuple_map = map(lambda x: x, circle_radiuses)
    circle_tuple = tuple(circle_tuple_map)
    
    # фильтрация
    radiuses_average = sum(circle_radiuses)/n
    
    circle_radiuses = list(filter(lambda x: x <= (radiuses_average * 1.1), circle_radiuses))
    
    # Объявление переменной для хранения перемноженных отфильтрованных значений
    radiuses_multiplication = 1
    
    for i in range(len(circle_radiuses)):
        radiuses_multiplication *= circle_radiuses[i]
        
    result = radiuses_multiplication/n # разделил перемножение на длину исходного массива 
    
    print(circle_radiuses)
    
    return result

n = input("Введите число прямоугольников: ")

if n is not int:
    raise Exception("Введите целочисленное значение")

if n <= 0:
    raise Exception("Введите число больше нуля")


lengths = []
widths = []
for i in range(n):
    rectangle_data = input(f"Введите длину и ширину прямоугольника №{i+1} через пробел: ")
    rectangle_data_list = rectangle_data.split(sep=" ")
    lengths.append(int(rectangle_data_list[0]))
    widths.append(int(rectangle_data_list[1]))
    

result = find_circle_around_rectangle(lenghts=lengths, widths=widths)
print(f"Function result = {result: .3f}")