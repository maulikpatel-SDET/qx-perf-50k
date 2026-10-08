"""Service module 39381: business logic, no crypto."""


def calculate_total_39381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39381():
    return 'module 39381 handles orders and invoices'
