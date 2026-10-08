"""Service module 25877: business logic, no crypto."""


def calculate_total_25877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25877():
    return 'module 25877 handles orders and invoices'
