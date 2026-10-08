"""Service module 14650: business logic, no crypto."""


def calculate_total_14650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14650():
    return 'module 14650 handles orders and invoices'
