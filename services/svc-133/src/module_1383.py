"""Service module 1383: business logic, no crypto."""


def calculate_total_1383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1383():
    return 'module 1383 handles orders and invoices'
