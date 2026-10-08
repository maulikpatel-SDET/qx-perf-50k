"""Service module 910: business logic, no crypto."""


def calculate_total_910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_910():
    return 'module 910 handles orders and invoices'
