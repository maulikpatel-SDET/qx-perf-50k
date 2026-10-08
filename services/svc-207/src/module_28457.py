"""Service module 28457: business logic, no crypto."""


def calculate_total_28457(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28457():
    return 'module 28457 handles orders and invoices'
