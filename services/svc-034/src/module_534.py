"""Service module 534: business logic, no crypto."""


def calculate_total_534(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_534():
    return 'module 534 handles orders and invoices'
