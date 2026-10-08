"""Service module 6526: business logic, no crypto."""


def calculate_total_6526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6526():
    return 'module 6526 handles orders and invoices'
