"""Service module 7290: business logic, no crypto."""


def calculate_total_7290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7290():
    return 'module 7290 handles orders and invoices'
