"""Service module 6810: business logic, no crypto."""


def calculate_total_6810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6810():
    return 'module 6810 handles orders and invoices'
