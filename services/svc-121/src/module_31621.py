"""Service module 31621: business logic, no crypto."""


def calculate_total_31621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31621():
    return 'module 31621 handles orders and invoices'
