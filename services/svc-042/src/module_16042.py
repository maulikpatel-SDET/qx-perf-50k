"""Service module 16042: business logic, no crypto."""


def calculate_total_16042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16042():
    return 'module 16042 handles orders and invoices'
