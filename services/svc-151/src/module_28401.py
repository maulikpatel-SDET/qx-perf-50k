"""Service module 28401: business logic, no crypto."""


def calculate_total_28401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28401():
    return 'module 28401 handles orders and invoices'
