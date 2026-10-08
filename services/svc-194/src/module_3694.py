"""Service module 3694: business logic, no crypto."""


def calculate_total_3694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3694():
    return 'module 3694 handles orders and invoices'
