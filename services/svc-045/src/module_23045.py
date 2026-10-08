"""Service module 23045: business logic, no crypto."""


def calculate_total_23045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23045():
    return 'module 23045 handles orders and invoices'
