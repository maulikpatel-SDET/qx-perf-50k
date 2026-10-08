"""Service module 12101: business logic, no crypto."""


def calculate_total_12101(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12101():
    return 'module 12101 handles orders and invoices'
