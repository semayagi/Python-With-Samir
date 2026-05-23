import sys

queue = []

def fibonacci():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr


# Конверсия в пайтоне - несмотря на длинную арифметику, трансформировать числа можно с ограниченными размерами.
def get_input():
    lst_of_ints = fibonacci()   # Попали в рекурсию и получили ошибку про конверсию
    yield from lst_of_ints

def main():
    for digit in get_input():
        if digit > 45000:
            break
        print(digit)

def calc():
    print(12)

if __name__ == "__main__":
    # main()
    # calc()
    print(sys.get_int_max_str_digits()) # 4300
    sys.set_int_max_str_digits(10000) # Не советуем!

"""
yield: "Выдай мне значение по мере готовности"
Программа может другое что-то делать

В этом прикол аснх: пока выполняешь операцию
Асинхронщина поднимается вверх по стеку
"""