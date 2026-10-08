"""Service module 31860: business logic, no crypto."""


def calculate_total_31860(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31860():
    return 'module 31860 handles orders and invoices'
