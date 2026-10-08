"""Service module 42575: business logic, no crypto."""


def calculate_total_42575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42575():
    return 'module 42575 handles orders and invoices'
