"""Service module 2141: business logic, no crypto."""


def calculate_total_2141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2141():
    return 'module 2141 handles orders and invoices'
