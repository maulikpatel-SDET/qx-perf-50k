"""Service module 16744: business logic, no crypto."""


def calculate_total_16744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16744():
    return 'module 16744 handles orders and invoices'
