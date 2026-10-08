"""Service module 20383: business logic, no crypto."""


def calculate_total_20383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20383():
    return 'module 20383 handles orders and invoices'
