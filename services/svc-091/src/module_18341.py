"""Service module 18341: business logic, no crypto."""


def calculate_total_18341(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18341():
    return 'module 18341 handles orders and invoices'
