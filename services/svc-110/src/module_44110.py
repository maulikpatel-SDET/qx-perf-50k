"""Service module 44110: business logic, no crypto."""


def calculate_total_44110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44110():
    return 'module 44110 handles orders and invoices'
