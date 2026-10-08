"""Service module 41703: business logic, no crypto."""


def calculate_total_41703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41703():
    return 'module 41703 handles orders and invoices'
