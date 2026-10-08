"""Service module 18833: business logic, no crypto."""


def calculate_total_18833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18833():
    return 'module 18833 handles orders and invoices'
