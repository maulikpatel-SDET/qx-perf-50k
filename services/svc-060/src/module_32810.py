"""Service module 32810: business logic, no crypto."""


def calculate_total_32810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32810():
    return 'module 32810 handles orders and invoices'
