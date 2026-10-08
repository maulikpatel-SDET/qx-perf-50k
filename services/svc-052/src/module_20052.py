"""Service module 20052: business logic, no crypto."""


def calculate_total_20052(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20052():
    return 'module 20052 handles orders and invoices'
