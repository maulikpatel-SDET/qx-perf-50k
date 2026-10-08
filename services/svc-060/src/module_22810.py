"""Service module 22810: business logic, no crypto."""


def calculate_total_22810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22810():
    return 'module 22810 handles orders and invoices'
