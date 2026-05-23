import sys

queue = []

def fibonacci():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr


def get_input():
    start = 1
    while start < 10000:
        data = yield start * 2
        start += data

def dummy_input():
    yield from get_input()

def main():
    generator = dummy_input() # Передай управление этому генератору!
    generator.send(None)
    while (start := input().strip()) != "q":
        print(generator.send(int(start)))

def calc():
    print(12)

if __name__ == "__main__":
    main()
    # calc()
    # print(sys.get_int_max_str_digits()) # 4300
    # sys.set_int_max_str_digits(10000) # Не советуем!

"""
yield: "Выдай мне значение по мере готовности"
Программа может другое что-то делать

В этом прикол аснх: пока выполняешь операцию
Асинхронщина поднимается вверх по стеку
Асинхронность заражает всё вверх по стеку
(если что-то ascyn, надо написать await)

Аналогично операторы

yield from в современном пайтоне видим очень редко
т.к. за его функционал сейчас отвечает асинхронщина
"""