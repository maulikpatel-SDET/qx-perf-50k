"""Service module 5940: business logic, no crypto."""


def calculate_total_5940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5940():
    return 'module 5940 handles orders and invoices'
