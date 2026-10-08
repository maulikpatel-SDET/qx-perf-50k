"""Service module 18464: business logic, no crypto."""


def calculate_total_18464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18464():
    return 'module 18464 handles orders and invoices'
