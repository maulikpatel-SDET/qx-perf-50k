"""Service module 36406: business logic, no crypto."""


def calculate_total_36406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36406():
    return 'module 36406 handles orders and invoices'
