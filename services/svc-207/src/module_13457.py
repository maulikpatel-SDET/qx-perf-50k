"""Service module 13457: business logic, no crypto."""


def calculate_total_13457(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13457():
    return 'module 13457 handles orders and invoices'
