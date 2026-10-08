"""Service module 16295: business logic, no crypto."""


def calculate_total_16295(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16295():
    return 'module 16295 handles orders and invoices'
