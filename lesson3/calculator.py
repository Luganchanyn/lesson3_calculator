#Найпростіший кальякулятор
#Запитуемо число
num1 = float(input("введіть перше число"))
#Запитуемо у користувача операцію
operation = input("введіть операцію (+,-,*,/):")
#Запитуемо друге число
num2 = float(input("введіть друге число"))
#Виконуемо обчислення
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Помилка: ділення на нуль!")
    result = num1 / num2
#Результат
print(f"Результат {result}")




