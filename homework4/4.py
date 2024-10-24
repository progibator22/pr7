try:
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))

    x = a * b + 4 * c

    print(f"Результат: x = {x}")

except ValueError:
    print("Ошибка: введено не число. Пожалуйста, введите корректные числовые значения.")
