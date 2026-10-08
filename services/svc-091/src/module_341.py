"""Service module 341: business logic, no crypto."""


def calculate_total_341(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_341():
    return 'module 341 handles orders and invoices'
