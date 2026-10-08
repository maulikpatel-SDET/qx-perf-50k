"""Service module 36657: business logic, no crypto."""


def calculate_total_36657(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36657():
    return 'module 36657 handles orders and invoices'
