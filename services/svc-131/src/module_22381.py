"""Service module 22381: business logic, no crypto."""


def calculate_total_22381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22381():
    return 'module 22381 handles orders and invoices'
