"""Service module 31670: business logic, no crypto."""


def calculate_total_31670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31670():
    return 'module 31670 handles orders and invoices'
