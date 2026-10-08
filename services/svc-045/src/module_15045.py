"""Service module 15045: business logic, no crypto."""


def calculate_total_15045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15045():
    return 'module 15045 handles orders and invoices'
