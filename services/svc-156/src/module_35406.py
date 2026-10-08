"""Service module 35406: business logic, no crypto."""


def calculate_total_35406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35406():
    return 'module 35406 handles orders and invoices'
