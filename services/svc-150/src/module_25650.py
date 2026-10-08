"""Service module 25650: business logic, no crypto."""


def calculate_total_25650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25650():
    return 'module 25650 handles orders and invoices'
