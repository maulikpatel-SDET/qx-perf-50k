"""Service module 47683: business logic, no crypto."""


def calculate_total_47683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47683():
    return 'module 47683 handles orders and invoices'
