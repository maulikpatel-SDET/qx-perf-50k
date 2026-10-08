"""Service module 41819: business logic, no crypto."""


def calculate_total_41819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41819():
    return 'module 41819 handles orders and invoices'
