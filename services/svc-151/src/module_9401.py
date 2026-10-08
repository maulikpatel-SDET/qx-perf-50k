"""Service module 9401: business logic, no crypto."""


def calculate_total_9401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9401():
    return 'module 9401 handles orders and invoices'
