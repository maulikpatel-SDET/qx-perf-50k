"""Service module 49819: business logic, no crypto."""


def calculate_total_49819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49819():
    return 'module 49819 handles orders and invoices'
