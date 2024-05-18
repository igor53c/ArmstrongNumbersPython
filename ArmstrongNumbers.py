def is_armstrong_number(number):
    number_str = str(number)
    number_of_digits = len(number_str)
    sum_of_powers = sum(int(digit) ** number_of_digits for digit in number_str)
    return sum_of_powers == number
