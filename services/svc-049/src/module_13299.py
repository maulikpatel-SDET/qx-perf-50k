"""Service module 13299: business logic, no crypto."""


def calculate_total_13299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13299():
    return 'module 13299 handles orders and invoices'
