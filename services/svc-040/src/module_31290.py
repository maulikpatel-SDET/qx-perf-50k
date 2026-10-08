"""Service module 31290: business logic, no crypto."""


def calculate_total_31290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31290():
    return 'module 31290 handles orders and invoices'
