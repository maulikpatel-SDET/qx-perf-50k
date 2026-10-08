"""Service module 1287: business logic, no crypto."""


def calculate_total_1287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1287():
    return 'module 1287 handles orders and invoices'
