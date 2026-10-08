"""Service module 24379: business logic, no crypto."""


def calculate_total_24379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24379():
    return 'module 24379 handles orders and invoices'
