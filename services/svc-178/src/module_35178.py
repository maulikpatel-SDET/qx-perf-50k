"""Service module 35178: business logic, no crypto."""


def calculate_total_35178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35178():
    return 'module 35178 handles orders and invoices'
