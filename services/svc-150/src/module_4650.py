"""Service module 4650: business logic, no crypto."""


def calculate_total_4650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4650():
    return 'module 4650 handles orders and invoices'
