"""Service module 12381: business logic, no crypto."""


def calculate_total_12381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12381():
    return 'module 12381 handles orders and invoices'
