"""Service module 18081: business logic, no crypto."""


def calculate_total_18081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18081():
    return 'module 18081 handles orders and invoices'
