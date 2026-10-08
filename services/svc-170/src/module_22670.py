"""Service module 22670: business logic, no crypto."""


def calculate_total_22670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22670():
    return 'module 22670 handles orders and invoices'
