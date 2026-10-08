"""Service module 42909: business logic, no crypto."""


def calculate_total_42909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42909():
    return 'module 42909 handles orders and invoices'
