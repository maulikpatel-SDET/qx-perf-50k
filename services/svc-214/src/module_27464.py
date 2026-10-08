"""Service module 27464: business logic, no crypto."""


def calculate_total_27464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27464():
    return 'module 27464 handles orders and invoices'
