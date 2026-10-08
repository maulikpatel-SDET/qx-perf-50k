"""Service module 10257: business logic, no crypto."""


def calculate_total_10257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10257():
    return 'module 10257 handles orders and invoices'
