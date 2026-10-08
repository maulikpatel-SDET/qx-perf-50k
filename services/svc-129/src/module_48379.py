"""Service module 48379: business logic, no crypto."""


def calculate_total_48379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48379():
    return 'module 48379 handles orders and invoices'
