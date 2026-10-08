"""Service module 47551: business logic, no crypto."""


def calculate_total_47551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47551():
    return 'module 47551 handles orders and invoices'
