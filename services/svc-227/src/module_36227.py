"""Service module 36227: business logic, no crypto."""


def calculate_total_36227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36227():
    return 'module 36227 handles orders and invoices'
