"""Service module 37819: business logic, no crypto."""


def calculate_total_37819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37819():
    return 'module 37819 handles orders and invoices'
