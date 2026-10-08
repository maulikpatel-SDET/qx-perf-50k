"""Service module 21406: business logic, no crypto."""


def calculate_total_21406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21406():
    return 'module 21406 handles orders and invoices'
