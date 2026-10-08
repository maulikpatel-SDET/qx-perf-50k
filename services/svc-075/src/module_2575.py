"""Service module 2575: business logic, no crypto."""


def calculate_total_2575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2575():
    return 'module 2575 handles orders and invoices'
