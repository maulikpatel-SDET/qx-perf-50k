"""Service module 13610: business logic, no crypto."""


def calculate_total_13610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13610():
    return 'module 13610 handles orders and invoices'
