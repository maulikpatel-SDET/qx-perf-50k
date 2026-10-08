"""Service module 3379: business logic, no crypto."""


def calculate_total_3379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3379():
    return 'module 3379 handles orders and invoices'
