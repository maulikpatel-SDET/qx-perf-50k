"""Service module 29575: business logic, no crypto."""


def calculate_total_29575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29575():
    return 'module 29575 handles orders and invoices'
