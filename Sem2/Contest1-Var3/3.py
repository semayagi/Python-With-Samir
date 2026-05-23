# Найти минимальную подстроку содержащую все символы данной строки с учётом кратности
# Пример: ("OLIIJOAKOLIJI" "JIIKL") -> "KOLIJI"
def symbols_check(s: str, t: str) -> bool:
    for c in set(t):
        if s.count(c) != t.count(c):
            return False
    return True

def min_cover_substring(s: str, t: str) -> str:
    i = 0
    j = len(s)
    for _ in range(len(s)):
        i += 1
        if not symbols_check(s[i:], t):
            i -= 1
            break
    for _ in range(i, len(s)):
        j -= 1
        if not symbols_check(s[i:j], t):
            j += 1
            break
    return s[i:j]

"""
Моё решение неверно - не находит минимального.

Пример Максима:

min_cover_substring("ABACB", "AB")
Указатель i на: A, B - всё окей
Но я пропустил минимальное решение - "AB"
Выдаст "ACB"
Решать надо методом двух указателей (скользящее окно?)

"""