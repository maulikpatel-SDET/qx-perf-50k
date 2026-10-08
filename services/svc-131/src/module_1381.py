"""Service module 1381: business logic, no crypto."""


def calculate_total_1381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1381():
    return 'module 1381 handles orders and invoices'
