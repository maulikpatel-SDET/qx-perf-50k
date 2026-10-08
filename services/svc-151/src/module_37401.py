"""Service module 37401: business logic, no crypto."""


def calculate_total_37401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37401():
    return 'module 37401 handles orders and invoices'
