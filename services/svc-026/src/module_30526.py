"""Service module 30526: business logic, no crypto."""


def calculate_total_30526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30526():
    return 'module 30526 handles orders and invoices'
