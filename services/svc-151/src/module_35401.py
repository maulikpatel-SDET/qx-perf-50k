"""Service module 35401: business logic, no crypto."""


def calculate_total_35401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35401():
    return 'module 35401 handles orders and invoices'
