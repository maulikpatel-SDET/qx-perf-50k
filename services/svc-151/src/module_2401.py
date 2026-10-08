"""Service module 2401: business logic, no crypto."""


def calculate_total_2401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2401():
    return 'module 2401 handles orders and invoices'
