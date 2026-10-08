"""Service module 7178: business logic, no crypto."""


def calculate_total_7178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7178():
    return 'module 7178 handles orders and invoices'
