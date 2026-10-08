"""Service module 36341: business logic, no crypto."""


def calculate_total_36341(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36341():
    return 'module 36341 handles orders and invoices'
