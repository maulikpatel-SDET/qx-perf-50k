"""Service module 19534: business logic, no crypto."""


def calculate_total_19534(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19534():
    return 'module 19534 handles orders and invoices'
