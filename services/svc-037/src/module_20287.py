"""Service module 20287: business logic, no crypto."""


def calculate_total_20287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20287():
    return 'module 20287 handles orders and invoices'
