def add_one(some_list):

    number = 0
    for num in some_list:
        number = number * 10 + num

    number = number + 1

    result = []
    for digit in str(number):
        result.append(int(digit))

    return result


assert add_one([1, 2, 3, 5]) == [1, 2, 3, 6], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")