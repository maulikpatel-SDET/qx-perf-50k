"""Service module 49670: business logic, no crypto."""


def calculate_total_49670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49670():
    return 'module 49670 handles orders and invoices'
