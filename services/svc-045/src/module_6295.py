"""Service module 6295: business logic, no crypto."""


def calculate_total_6295(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6295():
    return 'module 6295 handles orders and invoices'
