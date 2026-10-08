"""Service module 41290: business logic, no crypto."""


def calculate_total_41290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41290():
    return 'module 41290 handles orders and invoices'
