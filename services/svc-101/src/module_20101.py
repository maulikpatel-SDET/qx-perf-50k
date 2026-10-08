"""Service module 20101: business logic, no crypto."""


def calculate_total_20101(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20101():
    return 'module 20101 handles orders and invoices'
