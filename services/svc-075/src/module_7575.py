"""Service module 7575: business logic, no crypto."""


def calculate_total_7575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7575():
    return 'module 7575 handles orders and invoices'
