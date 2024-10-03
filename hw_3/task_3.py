
# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]


numbers = [1]


if len(numbers) % 2 == 0:
    first_mass = numbers[:len(numbers) // 2]
    second_mass = numbers[len(numbers) // 2:]
    result = first_mass, second_mass
    print(result)

elif len(numbers) % 2 != 0:
    first_mass = numbers[:(len(numbers) + 1) // 2]
    second_mass = numbers[(len(numbers) + 1) // 2:]
    result = first_mass, second_mass
    print(result)
else:
    first_mass = numbers[:len(numbers)]
    second_mass = numbers[:len(numbers)]
    result = first_mass, second_mass
    print(result)


