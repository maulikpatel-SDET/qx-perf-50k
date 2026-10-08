"""Service module 19940: business logic, no crypto."""


def calculate_total_19940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19940():
    return 'module 19940 handles orders and invoices'
