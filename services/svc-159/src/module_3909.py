"""Service module 3909: business logic, no crypto."""


def calculate_total_3909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3909():
    return 'module 3909 handles orders and invoices'
