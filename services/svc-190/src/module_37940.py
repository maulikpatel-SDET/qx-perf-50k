"""Service module 37940: business logic, no crypto."""


def calculate_total_37940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37940():
    return 'module 37940 handles orders and invoices'
