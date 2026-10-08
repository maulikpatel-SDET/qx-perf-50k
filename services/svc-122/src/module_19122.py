"""Service module 19122: business logic, no crypto."""


def calculate_total_19122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19122():
    return 'module 19122 handles orders and invoices'
