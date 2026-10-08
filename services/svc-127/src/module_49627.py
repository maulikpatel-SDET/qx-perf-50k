"""Service module 49627: business logic, no crypto."""


def calculate_total_49627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49627():
    return 'module 49627 handles orders and invoices'
