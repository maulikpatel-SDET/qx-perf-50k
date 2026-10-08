"""Service module 12820: business logic, no crypto."""


def calculate_total_12820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12820():
    return 'module 12820 handles orders and invoices'
