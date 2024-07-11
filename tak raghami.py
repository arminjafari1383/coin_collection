def single_digit_sum(number):
    while number >= 10:
        digits = [int(digit) for digit in str(number)] 
        number = sum(digits)
    return number
input_number = int(input(""))
result = single_digit_sum(input_number)
print(f"{result}")