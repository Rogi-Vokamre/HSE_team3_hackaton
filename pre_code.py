# Итоговое задание № 1 - задача № 1 со звездочкой "Функция-генератор yield"
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

max_value = int(input("Введите число, до которого будем считать: "))

for number in count_up_to(max_value):
    print(number)


# Итоговое задание № 1 - задача № 1 "Функция для чисел Фибоначчи"
def fib(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Введите номер числа Фибоначчи, на котором следует остановиться: "))

print(fib(n))