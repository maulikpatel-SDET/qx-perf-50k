"""Service module 17141: business logic, no crypto."""


def calculate_total_17141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17141():
    return 'module 17141 handles orders and invoices'
