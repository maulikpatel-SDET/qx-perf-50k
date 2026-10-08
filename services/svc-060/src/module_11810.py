"""Service module 11810: business logic, no crypto."""


def calculate_total_11810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11810():
    return 'module 11810 handles orders and invoices'
