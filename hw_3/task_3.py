# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]


numbers = [1, 2, 3, 4, 5, 6]

# Если массив у нас пустой, то создаем 2 пустых массива
if len(numbers) == 0:
    first_mass = numbers[:len(numbers)]
    second_mass = numbers[:len(numbers)]
    result = [first_mass, second_mass]
    print(result)
# Если массив четный, делим его пополам и разбиваем на 2 половины
elif len(numbers) % 2 == 0:
    first_mass = numbers[:len(numbers) // 2]
    second_mass = numbers[len(numbers) // 2:]
    result = [first_mass, second_mass]
    print(result)
# Если массив нечетный, делим его, добавляем один элемент к первой половине. Вторая половина начинается с оставшихся элементов
elif len(numbers) % 2 != 0:
    first_mass = numbers[:(len(numbers) + 1) // 2]
    second_mass = numbers[(len(numbers) + 1) // 2:]
    result = [first_mass, second_mass]
    print(result)