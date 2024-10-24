def decimal_to_binary(number):
    is_negative = number < 0
    number = abs(number)
    
    integer_part = int(number)
    fractional_part = number - integer_part

    binary_integer_part = bin(integer_part)[2:]
    
    binary_fractional_part = ""
    while fractional_part > 0 and len(binary_fractional_part) < 10:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional_part += str(bit)
        fractional_part -= bit

    binary_result = binary_integer_part
    if binary_fractional_part:
        binary_result += "." + binary_fractional_part

    if is_negative:
        binary_result = "-" + binary_result

    return binary_result


def decimal_to_octal(number):
    is_negative = number < 0
    number = abs(number)
    
    integer_part = int(number)
    fractional_part = number - integer_part

    octal_integer_part = oct(integer_part)[2:]
    
    octal_fractional_part = ""
    while fractional_part > 0 and len(octal_fractional_part) < 10:
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fractional_part += str(digit)
        fractional_part -= digit

    octal_result = octal_integer_part
    if octal_fractional_part:
        octal_result += "." + octal_fractional_part

    if is_negative:
        octal_result = "-" + octal_result

    return octal_result


try:
    decimal_number = float(input("Введите десятичное число: "))

    binary_number = decimal_to_binary(decimal_number)
    print(f"Двоичное представление: {binary_number}")

    octal_number = decimal_to_octal(decimal_number)
    print(f"Восьмеричное представление: {octal_number}")

except ValueError:
    print("Ошибка: введено не число. Пожалуйста, введите десятичное число.")
