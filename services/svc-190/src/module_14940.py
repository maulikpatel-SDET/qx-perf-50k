"""Service module 14940: business logic, no crypto."""


def calculate_total_14940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14940():
    return 'module 14940 handles orders and invoices'
