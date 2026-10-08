"""Service module 27534: business logic, no crypto."""


def calculate_total_27534(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27534():
    return 'module 27534 handles orders and invoices'
