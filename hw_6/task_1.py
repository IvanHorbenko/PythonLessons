import string

test_values = "a-a"


letters = string.ascii_letters

# Разделяем входную строку на две буквы
start, end = test_values.split('-')

# Получаем индексы начальной и конечной буквы
start_index = letters.index(start)
end_index = letters.index(end)

# Выводим все буквы от start до end включительно
print(letters[start_index:end_index + 1])