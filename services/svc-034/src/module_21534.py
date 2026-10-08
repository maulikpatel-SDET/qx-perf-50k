"""Service module 21534: business logic, no crypto."""


def calculate_total_21534(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21534():
    return 'module 21534 handles orders and invoices'
