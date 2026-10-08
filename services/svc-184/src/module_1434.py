"""Service module 1434: business logic, no crypto."""


def calculate_total_1434(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1434():
    return 'module 1434 handles orders and invoices'
