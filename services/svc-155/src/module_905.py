"""Service module 905: business logic, no crypto."""


def calculate_total_905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_905():
    return 'module 905 handles orders and invoices'
