"""Service module 1559: business logic, no crypto."""


def calculate_total_1559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1559():
    return 'module 1559 handles orders and invoices'
