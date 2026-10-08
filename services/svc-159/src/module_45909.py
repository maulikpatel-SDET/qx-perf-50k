"""Service module 45909: business logic, no crypto."""


def calculate_total_45909(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45909():
    return 'module 45909 handles orders and invoices'
