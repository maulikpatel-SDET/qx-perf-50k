"""Service module 13575: business logic, no crypto."""


def calculate_total_13575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13575():
    return 'module 13575 handles orders and invoices'
