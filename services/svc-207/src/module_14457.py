"""Service module 14457: business logic, no crypto."""


def calculate_total_14457(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14457():
    return 'module 14457 handles orders and invoices'
