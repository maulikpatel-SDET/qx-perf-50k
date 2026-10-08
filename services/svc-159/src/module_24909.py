"""Service module 24909: business logic, no crypto."""


def calculate_total_24909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24909():
    return 'module 24909 handles orders and invoices'
