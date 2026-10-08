"""Service module 15534: business logic, no crypto."""


def calculate_total_15534(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15534():
    return 'module 15534 handles orders and invoices'
