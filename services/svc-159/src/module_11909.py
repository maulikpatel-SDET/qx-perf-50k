"""Service module 11909: business logic, no crypto."""


def calculate_total_11909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11909():
    return 'module 11909 handles orders and invoices'
