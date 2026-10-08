"""Service module 41401: business logic, no crypto."""


def calculate_total_41401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41401():
    return 'module 41401 handles orders and invoices'
