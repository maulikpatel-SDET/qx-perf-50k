"""Service module 28819: business logic, no crypto."""


def calculate_total_28819(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28819():
    return 'module 28819 handles orders and invoices'
