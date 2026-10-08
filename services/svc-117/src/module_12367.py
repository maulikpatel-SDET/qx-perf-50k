"""Service module 12367: business logic, no crypto."""


def calculate_total_12367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12367():
    return 'module 12367 handles orders and invoices'
