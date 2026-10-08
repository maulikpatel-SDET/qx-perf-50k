"""Service module 47670: business logic, no crypto."""


def calculate_total_47670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47670():
    return 'module 47670 handles orders and invoices'
