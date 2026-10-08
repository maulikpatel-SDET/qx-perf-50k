"""Service module 17670: business logic, no crypto."""


def calculate_total_17670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17670():
    return 'module 17670 handles orders and invoices'
