"""Service module 14575: business logic, no crypto."""


def calculate_total_14575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14575():
    return 'module 14575 handles orders and invoices'
