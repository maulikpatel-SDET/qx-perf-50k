"""Service module 48290: business logic, no crypto."""


def calculate_total_48290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48290():
    return 'module 48290 handles orders and invoices'
