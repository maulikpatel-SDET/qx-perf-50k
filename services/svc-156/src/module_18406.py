"""Service module 18406: business logic, no crypto."""


def calculate_total_18406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18406():
    return 'module 18406 handles orders and invoices'
