# Вернуть значение, в котором функция "стабильна", то есть func(value) == value
def iterate_until_stable(func, value):
    while (func(value) != value):
        value = func(value)
    return value