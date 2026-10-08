"""Service module 40880: business logic, no crypto."""


def calculate_total_40880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40880():
    return 'module 40880 handles orders and invoices'
