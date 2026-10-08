"""Service module 30141: business logic, no crypto."""


def calculate_total_30141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30141():
    return 'module 30141 handles orders and invoices'
