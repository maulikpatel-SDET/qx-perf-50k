"""Service module 48940: business logic, no crypto."""


def calculate_total_48940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48940():
    return 'module 48940 handles orders and invoices'
