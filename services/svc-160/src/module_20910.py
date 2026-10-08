"""Service module 20910: business logic, no crypto."""


def calculate_total_20910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20910():
    return 'module 20910 handles orders and invoices'
