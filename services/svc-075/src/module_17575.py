"""Service module 17575: business logic, no crypto."""


def calculate_total_17575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17575():
    return 'module 17575 handles orders and invoices'
