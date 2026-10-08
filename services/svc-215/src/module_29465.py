"""Service module 29465: business logic, no crypto."""


def calculate_total_29465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29465():
    return 'module 29465 handles orders and invoices'
