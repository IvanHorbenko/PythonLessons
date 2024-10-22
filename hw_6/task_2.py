
seconds = int(input("Введите значение seconds : "))


days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дня"
else:
    day_word = "дней"


final_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(final_time)
