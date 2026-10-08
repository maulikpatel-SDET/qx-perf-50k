"""Service module 3905: business logic, no crypto."""


def calculate_total_3905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3905():
    return 'module 3905 handles orders and invoices'
