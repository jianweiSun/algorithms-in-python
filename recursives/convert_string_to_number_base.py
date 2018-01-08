
def convert_string(number, base_string):
    assert isinstance(number, int) and isinstance(base_string, str)
    base = len(base_string)

    result = str()
    while number > 0:
        result = base_string[number % base] + result
        number = number // base

    return result


def convert_string_recursive(number, base_string):
    assert isinstance(number, int) and isinstance(base_string, str)
    base = len(base_string)

    if number < base:
        return base_string[number]
    else:
        return convert_string_recursive(number // base, base_string) + base_string[number % base]
