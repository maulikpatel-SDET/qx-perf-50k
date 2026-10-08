"""Service module 9551: business logic, no crypto."""


def calculate_total_9551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9551():
    return 'module 9551 handles orders and invoices'
