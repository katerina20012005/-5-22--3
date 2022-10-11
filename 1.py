# Найти количество элементов в заданном массиве ARRAY,
# отличающихся от минимального на DELTA
# Комментарий: array = [1,2,3,5] delta = 4 Вывод: 1

array = [0, 2, 3, 5, 1, 2, 3, 5, 6, 7]
delta = int(input("Введи значение DELTA: "))
result = array.count(min(array) + delta)
print(result)