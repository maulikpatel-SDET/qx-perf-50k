"""Service module 13122: business logic, no crypto."""


def calculate_total_13122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13122():
    return 'module 13122 handles orders and invoices'
