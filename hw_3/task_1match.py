# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!
# Решение через match

# Просим пользователя ввести первое число
number1 = int(input("Введите первое число: "))
# Просим пользователя ввести номер исходя из операции, которую он хочет произвести
operatorValue = int(input("1. + (сложить)\n2. - (отнять)\n3. * (умножить)\n4. / (разделить)\nВведите номер исходя из предложеных: "))
# Просим пользователя ввести второе число
number2 = int(input("Введите второе число: "))

match operatorValue:
match operatorValue:
    # Если пользватель ввел значение оператора 1, то будет выполняться сложение
    case 1:
        print(number1 + number2)
        # Если пользватель ввел значение оператора 2, то будет выполняться вычетание
    case 2:
        print(number1 - number2)
        # Если пользватель ввел значение оператора 3, то будет выполняться умножение
    case 3:
        print(number1 * number2)
        # Если пользватель ввел значение оператора 4, то будет выполняться деление
    case 4:
        # Проверяем, что если второе число не равно 0, то програма выполнит деление
        if number2 != 0:
            print(number1 / number2)
        # Если второе число равно 0, то выводим сообщение, что делить на ноль нельзя
        else:
            print("На ноль делить нельзя")