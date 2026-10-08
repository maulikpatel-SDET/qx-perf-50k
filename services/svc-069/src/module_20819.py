"""Service module 20819: business logic, no crypto."""


def calculate_total_20819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20819():
    return 'module 20819 handles orders and invoices'
