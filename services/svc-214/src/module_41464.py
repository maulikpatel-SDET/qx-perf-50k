"""Service module 41464: business logic, no crypto."""


def calculate_total_41464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41464():
    return 'module 41464 handles orders and invoices'
