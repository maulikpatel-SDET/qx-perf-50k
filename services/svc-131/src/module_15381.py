"""Service module 15381: business logic, no crypto."""


def calculate_total_15381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15381():
    return 'module 15381 handles orders and invoices'
