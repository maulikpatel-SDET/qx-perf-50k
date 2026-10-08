"""Service module 30909: business logic, no crypto."""


def calculate_total_30909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30909():
    return 'module 30909 handles orders and invoices'
