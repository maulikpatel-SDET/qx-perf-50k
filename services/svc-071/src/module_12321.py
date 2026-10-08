"""Service module 12321: business logic, no crypto."""


def calculate_total_12321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12321():
    return 'module 12321 handles orders and invoices'
