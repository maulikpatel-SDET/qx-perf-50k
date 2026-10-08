"""Service module 27468: business logic, no crypto."""


def calculate_total_27468(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27468():
    return 'module 27468 handles orders and invoices'
