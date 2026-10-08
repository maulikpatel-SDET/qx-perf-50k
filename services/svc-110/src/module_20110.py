"""Service module 20110: business logic, no crypto."""


def calculate_total_20110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20110():
    return 'module 20110 handles orders and invoices'
