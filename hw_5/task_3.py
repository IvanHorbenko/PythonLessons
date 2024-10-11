import string

input_str = "t!e@s#t t%e^s&t"

# Заменяю string.punctuation на ""
for char in string.punctuation:
    input_str = input_str.replace(char, "")

# Разделяем строку на слова
split_words = input_str.split()

# Делаем каждое слово с заглавной буквы
result = ""
for word in split_words:
    result += word.capitalize()

# Добавляем символ '#' в начало строки
input_str = "#" + result

# Обрезаем если итогово больше 140
if len(input_str) > 140:
    input_str = input_str[:140]

print(input_str)
