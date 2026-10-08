"""Service module 39909: business logic, no crypto."""


def calculate_total_39909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39909():
    return 'module 39909 handles orders and invoices'
