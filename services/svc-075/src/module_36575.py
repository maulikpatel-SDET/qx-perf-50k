"""Service module 36575: business logic, no crypto."""


def calculate_total_36575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36575():
    return 'module 36575 handles orders and invoices'
