"""Service module 38735: business logic, no crypto."""


def calculate_total_38735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38735():
    return 'module 38735 handles orders and invoices'
