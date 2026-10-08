"""Service module 16910: business logic, no crypto."""


def calculate_total_16910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16910():
    return 'module 16910 handles orders and invoices'
