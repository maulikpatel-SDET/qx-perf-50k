"""Service module 14910: business logic, no crypto."""


def calculate_total_14910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14910():
    return 'module 14910 handles orders and invoices'
