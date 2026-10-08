"""Service module 450: business logic, no crypto."""


def calculate_total_450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_450():
    return 'module 450 handles orders and invoices'
