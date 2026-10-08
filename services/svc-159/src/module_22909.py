"""Service module 22909: business logic, no crypto."""


def calculate_total_22909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22909():
    return 'module 22909 handles orders and invoices'
