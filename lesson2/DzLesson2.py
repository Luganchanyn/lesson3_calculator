# Запитуємо у користувача 4-значне число
number = int(input( "Введіть 4-значне число:" ))
# Визначаємо кожну цифру числа
thousands = number // 1000
hunders = (number // 100) %10
tens = (number // 10) % 10
units = number % 10
# Виводимо цифри на окремих рядках
print(thousands)
print(hunders)
print(tens)
print(units)