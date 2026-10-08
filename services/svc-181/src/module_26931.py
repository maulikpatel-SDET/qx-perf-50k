"""Service module 26931: business logic, no crypto."""


def calculate_total_26931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26931():
    return 'module 26931 handles orders and invoices'
