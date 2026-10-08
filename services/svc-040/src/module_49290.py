"""Service module 49290: business logic, no crypto."""


def calculate_total_49290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49290():
    return 'module 49290 handles orders and invoices'
