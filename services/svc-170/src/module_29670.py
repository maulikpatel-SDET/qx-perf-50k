"""Service module 29670: business logic, no crypto."""


def calculate_total_29670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29670():
    return 'module 29670 handles orders and invoices'
