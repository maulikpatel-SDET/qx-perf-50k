"""Service module 25986: business logic, no crypto."""


def calculate_total_25986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25986():
    return 'module 25986 handles orders and invoices'
