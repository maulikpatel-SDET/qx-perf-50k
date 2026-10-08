"""Service module 3457: business logic, no crypto."""


def calculate_total_3457(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3457():
    return 'module 3457 handles orders and invoices'
