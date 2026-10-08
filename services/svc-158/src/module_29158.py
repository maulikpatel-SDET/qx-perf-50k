"""Service module 29158: business logic, no crypto."""


def calculate_total_29158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29158():
    return 'module 29158 handles orders and invoices'
