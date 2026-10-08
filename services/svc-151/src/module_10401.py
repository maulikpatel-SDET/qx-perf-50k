"""Service module 10401: business logic, no crypto."""


def calculate_total_10401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10401():
    return 'module 10401 handles orders and invoices'
