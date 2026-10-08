"""Service module 38464: business logic, no crypto."""


def calculate_total_38464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38464():
    return 'module 38464 handles orders and invoices'
