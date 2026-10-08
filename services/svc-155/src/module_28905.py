"""Service module 28905: business logic, no crypto."""


def calculate_total_28905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28905():
    return 'module 28905 handles orders and invoices'
