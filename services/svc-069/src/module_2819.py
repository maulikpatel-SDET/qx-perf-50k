"""Service module 2819: business logic, no crypto."""


def calculate_total_2819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2819():
    return 'module 2819 handles orders and invoices'
