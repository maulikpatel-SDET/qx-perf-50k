"""Service module 10880: business logic, no crypto."""


def calculate_total_10880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10880():
    return 'module 10880 handles orders and invoices'
