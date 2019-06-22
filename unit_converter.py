symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


# divide the fractional part of a number and return it as integer
# if the fractional part does not exist, return None
def get_fractional_part(number):
    number = str(number)
    dot_index = number.find('.')
    if dot_index == -1:
        return None
    fraction_part = int(number[dot_index+1::])
    return fraction_part


# convert any decimal number to any base, only works with base-2 up to base-36 (all alphabetical letters)
# if you add more symbols in the symbols tuple, more available bases are added too
def integer_decimal_to_any_base(number, base):
    # to avoid crash whit floating's numbers
    number = int(number)
    if number == 0:
        return 0
    result = ""
    while not number == 0:
        result = result + symbols[number % base]
        number = number // base
    # reverse the result to be correct
    result = result[::-1]
    return result


# does practically the same as integer converter, but works with floating numbers
def floating_decimal_to_any_base(number, base):
    integer_part = int(number)
    fractional_part = get_fractional_part(number)
    fractional_part = 0 if not fractional_part else fractional_part
    result = "{}.{}".format(
        integer_decimal_to_any_base(integer_part, base),
        integer_decimal_to_any_base(fractional_part, base)
    )
    return result


# check if the number is integer or floating and convert whit correct method
def decimal_to_any_base(number, base):
    # check if the number is floating or integer
    if int(number) == number:
        return integer_decimal_to_any_base(number, base)
    else:
        return floating_decimal_to_any_base(number, base)