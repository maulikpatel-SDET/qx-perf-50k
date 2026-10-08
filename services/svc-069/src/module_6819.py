"""Service module 6819: business logic, no crypto."""


def calculate_total_6819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6819():
    return 'module 6819 handles orders and invoices'
