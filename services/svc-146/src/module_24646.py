"""Service module 24646: business logic, no crypto."""


def calculate_total_24646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24646():
    return 'module 24646 handles orders and invoices'
