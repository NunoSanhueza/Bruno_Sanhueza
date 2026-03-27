def add(a, b):
    return (a + b)


def divide(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b


def get_element(list_, index):
    return list_[index ]


def convert_to_integer(value):
    return int(float(value))
