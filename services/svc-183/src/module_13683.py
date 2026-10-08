"""Service module 13683: business logic, no crypto."""


def calculate_total_13683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13683():
    return 'module 13683 handles orders and invoices'
