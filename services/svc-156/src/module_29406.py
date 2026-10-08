"""Service module 29406: business logic, no crypto."""


def calculate_total_29406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29406():
    return 'module 29406 handles orders and invoices'
