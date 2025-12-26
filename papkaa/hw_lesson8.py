print("Задание 1")
print("Подсчёт ИМТ")

try:
    height = int(input("Введите ваш рост "))
except:
    print("Неправильно введены данные. Укажите численное значение.")
try:
    weight = int(input("Введите ваш вес "))
except:
    print("Неправильно введены данные. Укажите численное значение.")

heightm = height / 100
imt = weight/(heightm*heightm)
print(f"Ваш индекс массы тела {imt:.2f}")

if imt < 20:
    print("У вас недостаточный вес")
elif imt >= 20 and imt <= 24:
    print("Ваш вес находится в пределах нормы")
elif imt >= 25 and imt <= 30:
    print("У вас незначительный избыток веса")
elif imt >= 31 and imt <= 40:
    print("У вас наблюдается склонность к ожирению")
elif imt > 40:
    print("У вас ожирение")

print("Задание 2")

try:
    num1 = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /, **, %): ")
    num2 = float(input("Введите второе число: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num1 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        result = num1 / num2
    elif operation == '**':
        result = num1 ** num2
    elif operation == '%':
        result = num1 % num2
    else:
        print(f"Ошибка: операция '{operation}' не поддерживается!")


    print(f"Результат: {num1} {operation} {num2} = {result}")

except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
