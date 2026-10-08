"""Service module 4141: business logic, no crypto."""


def calculate_total_4141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4141():
    return 'module 4141 handles orders and invoices'
