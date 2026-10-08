"""Service module 10457: business logic, no crypto."""


def calculate_total_10457(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10457():
    return 'module 10457 handles orders and invoices'
