"""Service module 1905: business logic, no crypto."""


def calculate_total_1905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1905():
    return 'module 1905 handles orders and invoices'
