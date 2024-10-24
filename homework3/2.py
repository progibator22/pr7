def decimal_to_ternary(number):
    is_negative = number < 0
    number = abs(number)
    
    integer_part = int(number)
    fractional_part = number - integer_part

    ternary_integer_part = ""
    if integer_part == 0:
        ternary_integer_part = "0"
    else:
        while integer_part > 0:
            ternary_integer_part = str(integer_part % 3) + ternary_integer_part
            integer_part //= 3

    ternary_fractional_part = ""
    while fractional_part > 0 and len(ternary_fractional_part) < 10:
        fractional_part *= 3
        digit = int(fractional_part)
        ternary_fractional_part += str(digit)
        fractional_part -= digit

    ternary_result = ternary_integer_part
    if ternary_fractional_part:
        ternary_result += "." + ternary_fractional_part

    if is_negative:
        ternary_result = "-" + ternary_result

    return ternary_result

try:
    decimal_number = float(input("Введите десятичное число: "))

    ternary_number = decimal_to_ternary(decimal_number)
    print(f"Троичное представление: {ternary_number}")

except ValueError:
    print("Ошибка: введено не число. Пожалуйста, введите десятичное число.")
