import string
import keyword

test_date =  [ "_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value",
            "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception" ]

for variable_name in test_date:
    print(f"{variable_name}: ", end="")

    # Проверка, что переменная не начинается с цифры
    if variable_name[0].isdigit():
        print(False)
        continue

    # Проверка на количество подчеркиваний (не более одного)
    if variable_name.count('_') > 1:
        print(False)
        continue

    # Проверка на использование ключевого слова
    if variable_name in keyword.kwlist:
        print(False)
        continue

    # Допустимые символы: строчные буквы, цифры и одно подчеркивание
    valid_chars = string.ascii_lowercase + string.digits + '_'

    # Проверка каждого символа
    invalid_char = False
    for char in variable_name:
        if char not in valid_chars:
            print(False)
            invalid_char = True
            break

    if not invalid_char:
        print(True)