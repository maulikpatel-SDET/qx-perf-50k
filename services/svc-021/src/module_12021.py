"""Service module 12021: business logic, no crypto."""


def calculate_total_12021(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12021():
    return 'module 12021 handles orders and invoices'
