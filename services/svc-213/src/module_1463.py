"""Service module 1463: business logic, no crypto."""


def calculate_total_1463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1463():
    return 'module 1463 handles orders and invoices'
