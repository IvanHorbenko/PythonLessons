# Получаем ввод от пользователя
user_input = input("Введите количество секунд от 0 до 8640000: ")

# Проверяем, что введено число и оно в нужном диапазоне
if user_input.isdigit() and 0 <= int(user_input) < 8640000:
    seconds = int(user_input)  # Присваиваем значение переменной seconds

    # Переводим секунды в дни, часы, минуты и секунды
    days = seconds // 86400  # Считаем количество полных дней
    seconds %= 86400  # Оставшиеся секунды после вычитания дней

    hours = seconds // 3600  # Считаем количество полных часов
    seconds %= 3600  # Оставшиеся секунды после вычитания часов

    minutes = seconds // 60  # Считаем количество полных минут
    seconds %= 60  # Оставшиеся секунды

    # Определяем, какое слово использовать для "день"
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дня"
    else:
        day_word = "дней"

    # Форматируем вывод
    final_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(final_time)
else:
    print("Пожалуйста, введите число от 0 до 8640000.")
