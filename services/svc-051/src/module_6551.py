"""Service module 6551: business logic, no crypto."""


def calculate_total_6551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6551():
    return 'module 6551 handles orders and invoices'
