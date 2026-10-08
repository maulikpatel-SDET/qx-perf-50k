"""Service module 20464: business logic, no crypto."""


def calculate_total_20464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20464():
    return 'module 20464 handles orders and invoices'
