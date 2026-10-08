"""Service module 47050: business logic, no crypto."""


def calculate_total_47050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47050():
    return 'module 47050 handles orders and invoices'
