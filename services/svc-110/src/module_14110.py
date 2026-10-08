"""Service module 14110: business logic, no crypto."""


def calculate_total_14110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14110():
    return 'module 14110 handles orders and invoices'
