n = int(input("Введите число: "))

while n > 9:
    result = 1
    for number in str(n):
        result = result * int(number)
    n = result
print(n)


