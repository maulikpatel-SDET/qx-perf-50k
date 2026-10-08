"""Service module 30122: business logic, no crypto."""


def calculate_total_30122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30122():
    return 'module 30122 handles orders and invoices'
