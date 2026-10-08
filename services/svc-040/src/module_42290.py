"""Service module 42290: business logic, no crypto."""


def calculate_total_42290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42290():
    return 'module 42290 handles orders and invoices'
