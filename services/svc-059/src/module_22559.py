"""Service module 22559: business logic, no crypto."""


def calculate_total_22559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22559():
    return 'module 22559 handles orders and invoices'
