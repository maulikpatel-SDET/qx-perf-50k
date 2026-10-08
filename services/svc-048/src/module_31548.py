"""Service module 31548: business logic, no crypto."""


def calculate_total_31548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31548():
    return 'module 31548 handles orders and invoices'
