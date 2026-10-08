"""Service module 29819: business logic, no crypto."""


def calculate_total_29819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29819():
    return 'module 29819 handles orders and invoices'
