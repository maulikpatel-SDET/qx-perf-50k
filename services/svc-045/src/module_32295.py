"""Service module 32295: business logic, no crypto."""


def calculate_total_32295(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32295():
    return 'module 32295 handles orders and invoices'
