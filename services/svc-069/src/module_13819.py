"""Service module 13819: business logic, no crypto."""


def calculate_total_13819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13819():
    return 'module 13819 handles orders and invoices'
