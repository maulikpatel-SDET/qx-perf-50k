"""Service module 37551: business logic, no crypto."""


def calculate_total_37551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37551():
    return 'module 37551 handles orders and invoices'
