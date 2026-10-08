"""Service module 8178: business logic, no crypto."""


def calculate_total_8178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8178():
    return 'module 8178 handles orders and invoices'
