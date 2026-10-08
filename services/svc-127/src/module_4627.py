"""Service module 4627: business logic, no crypto."""


def calculate_total_4627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4627():
    return 'module 4627 handles orders and invoices'
