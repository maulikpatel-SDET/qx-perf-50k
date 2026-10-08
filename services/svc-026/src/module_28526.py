"""Service module 28526: business logic, no crypto."""


def calculate_total_28526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28526():
    return 'module 28526 handles orders and invoices'
