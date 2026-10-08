"""Service module 33406: business logic, no crypto."""


def calculate_total_33406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33406():
    return 'module 33406 handles orders and invoices'
