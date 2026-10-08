"""Service module 30744: business logic, no crypto."""


def calculate_total_30744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30744():
    return 'module 30744 handles orders and invoices'
