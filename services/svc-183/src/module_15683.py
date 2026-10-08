"""Service module 15683: business logic, no crypto."""


def calculate_total_15683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15683():
    return 'module 15683 handles orders and invoices'
