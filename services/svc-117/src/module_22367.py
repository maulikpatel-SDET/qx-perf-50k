"""Service module 22367: business logic, no crypto."""


def calculate_total_22367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22367():
    return 'module 22367 handles orders and invoices'
