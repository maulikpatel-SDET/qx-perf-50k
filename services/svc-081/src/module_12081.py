"""Service module 12081: business logic, no crypto."""


def calculate_total_12081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12081():
    return 'module 12081 handles orders and invoices'
