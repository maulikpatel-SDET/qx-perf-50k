"""Service module 47548: business logic, no crypto."""


def calculate_total_47548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47548():
    return 'module 47548 handles orders and invoices'
