"""Service module 17122: business logic, no crypto."""


def calculate_total_17122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17122():
    return 'module 17122 handles orders and invoices'
