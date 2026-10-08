"""Service module 8909: business logic, no crypto."""


def calculate_total_8909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8909():
    return 'module 8909 handles orders and invoices'
