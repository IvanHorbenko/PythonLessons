while True:
    number1 = int(input("Введите первое число: "))
    # Просим пользователя ввести оператор
    operatorValue = input("Введите оператор (+, -, *, /): ")
    # Просим пользователя ввести второе число
    number2 = int(input("Введите второе число: "))

    # В зависимости от выбранного оператора, выбираем какое действие будет происходить
    if operatorValue == "+":
        print(number1 + number2)
    elif operatorValue == "-":
        print(number1 - number2)
    elif operatorValue == "*":
        print(number1 * number2)
    elif operatorValue == "/":
        # Проверяем, что если второе число не равно 0, то програма выполнит деление
        if number2 != 0:
            print(number1 / number2)
        # Если второе число равно 0, то выводим сообщение, что делить на ноль нельзя
        else:
            print("На ноль делить нельзя")

    # Запрашиваем, хочет ли пользователь продолжить
    continue_calculation = input("Хотите продолжить? (y/n): ")
    if continue_calculation != 'y':
        print("Досвидания!")
        break
