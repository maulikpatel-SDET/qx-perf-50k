"""Service module 78: business logic, no crypto."""


def calculate_total_78(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_78():
    return 'module 78 handles orders and invoices'
