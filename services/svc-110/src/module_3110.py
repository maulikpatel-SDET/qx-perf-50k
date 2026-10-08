"""Service module 3110: business logic, no crypto."""


def calculate_total_3110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3110():
    return 'module 3110 handles orders and invoices'
