"""Service module 24295: business logic, no crypto."""


def calculate_total_24295(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24295():
    return 'module 24295 handles orders and invoices'
