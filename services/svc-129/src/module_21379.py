"""Service module 21379: business logic, no crypto."""


def calculate_total_21379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21379():
    return 'module 21379 handles orders and invoices'
