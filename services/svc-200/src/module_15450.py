"""Service module 15450: business logic, no crypto."""


def calculate_total_15450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15450():
    return 'module 15450 handles orders and invoices'
