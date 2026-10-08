"""Service module 22999: business logic, no crypto."""


def calculate_total_22999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22999():
    return 'module 22999 handles orders and invoices'
