"""Service module 23122: business logic, no crypto."""


def calculate_total_23122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23122():
    return 'module 23122 handles orders and invoices'
