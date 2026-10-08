"""Service module 36940: business logic, no crypto."""


def calculate_total_36940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36940():
    return 'module 36940 handles orders and invoices'
