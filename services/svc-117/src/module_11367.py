"""Service module 11367: business logic, no crypto."""


def calculate_total_11367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11367():
    return 'module 11367 handles orders and invoices'
