"""Service module 14735: business logic, no crypto."""


def calculate_total_14735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14735():
    return 'module 14735 handles orders and invoices'
