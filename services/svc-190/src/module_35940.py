"""Service module 35940: business logic, no crypto."""


def calculate_total_35940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35940():
    return 'module 35940 handles orders and invoices'
