"""Service module 39526: business logic, no crypto."""


def calculate_total_39526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39526():
    return 'module 39526 handles orders and invoices'
