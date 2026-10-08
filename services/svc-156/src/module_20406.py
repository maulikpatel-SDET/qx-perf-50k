"""Service module 20406: business logic, no crypto."""


def calculate_total_20406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20406():
    return 'module 20406 handles orders and invoices'
