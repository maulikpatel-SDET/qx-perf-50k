"""Service module 38401: business logic, no crypto."""


def calculate_total_38401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38401():
    return 'module 38401 handles orders and invoices'
