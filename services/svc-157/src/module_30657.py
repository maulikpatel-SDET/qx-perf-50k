"""Service module 30657: business logic, no crypto."""


def calculate_total_30657(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30657():
    return 'module 30657 handles orders and invoices'
