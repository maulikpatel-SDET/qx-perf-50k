"""Service module 25551: business logic, no crypto."""


def calculate_total_25551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25551():
    return 'module 25551 handles orders and invoices'
