"""Service module 20551: business logic, no crypto."""


def calculate_total_20551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20551():
    return 'module 20551 handles orders and invoices'
