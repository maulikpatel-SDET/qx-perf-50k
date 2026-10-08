"""Service module 49110: business logic, no crypto."""


def calculate_total_49110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49110():
    return 'module 49110 handles orders and invoices'
