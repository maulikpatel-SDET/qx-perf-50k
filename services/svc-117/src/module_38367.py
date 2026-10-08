"""Service module 38367: business logic, no crypto."""


def calculate_total_38367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38367():
    return 'module 38367 handles orders and invoices'
