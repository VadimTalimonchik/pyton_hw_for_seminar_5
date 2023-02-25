# Задача 28.
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

print()
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print()

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

print('Сумма чисел', a, 'и', b, 'равна', sum(a, b))
print()
