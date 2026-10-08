"""Service module 1694: business logic, no crypto."""


def calculate_total_1694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1694():
    return 'module 1694 handles orders and invoices'
