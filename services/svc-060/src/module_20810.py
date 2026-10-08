"""Service module 20810: business logic, no crypto."""


def calculate_total_20810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20810():
    return 'module 20810 handles orders and invoices'
