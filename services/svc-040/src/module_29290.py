"""Service module 29290: business logic, no crypto."""


def calculate_total_29290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29290():
    return 'module 29290 handles orders and invoices'
