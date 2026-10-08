"""Service module 1122: business logic, no crypto."""


def calculate_total_1122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1122():
    return 'module 1122 handles orders and invoices'
