"""Service module 56: business logic, no crypto."""


def calculate_total_56(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_56():
    return 'module 56 handles orders and invoices'
