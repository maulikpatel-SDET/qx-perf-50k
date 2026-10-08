"""Service module 28295: business logic, no crypto."""


def calculate_total_28295(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28295():
    return 'module 28295 handles orders and invoices'
