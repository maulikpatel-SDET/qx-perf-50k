"""Service module 38575: business logic, no crypto."""


def calculate_total_38575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38575():
    return 'module 38575 handles orders and invoices'
