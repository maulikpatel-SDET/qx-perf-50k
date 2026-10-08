"""Service module 12610: business logic, no crypto."""


def calculate_total_12610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12610():
    return 'module 12610 handles orders and invoices'
