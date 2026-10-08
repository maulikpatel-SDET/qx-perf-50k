"""Service module 3575: business logic, no crypto."""


def calculate_total_3575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3575():
    return 'module 3575 handles orders and invoices'
