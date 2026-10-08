"""Service module 37141: business logic, no crypto."""


def calculate_total_37141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37141():
    return 'module 37141 handles orders and invoices'
