"""Service module 38819: business logic, no crypto."""


def calculate_total_38819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38819():
    return 'module 38819 handles orders and invoices'
