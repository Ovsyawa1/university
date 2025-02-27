from statistics import median


## Задание №6 ##

def create_list(start: int, stop: int, step: int):
    my_arr = []
    k = 0 # итератор для количества чичел кратных 7
    for i in range(start, stop, step):
        if i % 7 == 0:
            k += 1
        my_arr.append(i)
        
    new_arr = list(filter(lambda x: x % 7 == 0, my_arr))
    
    arr_median = median(my_arr)
    my_result = k - arr_median
    
    if my_result < 0:
        new_arr.sort(reverse=True)
    elif my_result > 0:
        my_arr_copy = new_arr.copy()
        my_arr_copy.insert(0, my_result)
        print(my_arr_copy)
    else:
        print("The result equals zero!")

    return new_arr

result_arr = create_list(6, 15, 1)
print(result_arr)