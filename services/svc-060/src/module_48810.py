"""Service module 48810: business logic, no crypto."""


def calculate_total_48810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48810():
    return 'module 48810 handles orders and invoices'
