"""Service module 14819: business logic, no crypto."""


def calculate_total_14819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14819():
    return 'module 14819 handles orders and invoices'
