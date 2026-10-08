"""Service module 36381: business logic, no crypto."""


def calculate_total_36381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36381():
    return 'module 36381 handles orders and invoices'
