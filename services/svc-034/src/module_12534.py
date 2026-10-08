"""Service module 12534: business logic, no crypto."""


def calculate_total_12534(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12534():
    return 'module 12534 handles orders and invoices'
