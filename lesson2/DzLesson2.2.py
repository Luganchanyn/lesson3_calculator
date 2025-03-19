# Запитуемо у користувача 5-значне число
number = int(input("Ведіть 5-значне число: "))
reversed_number = int(str(number)[::-1])
# Виводимо результат
print(f"Число в зворотньму порядку{reversed_number}")