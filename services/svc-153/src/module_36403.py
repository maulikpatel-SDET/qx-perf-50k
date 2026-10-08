"""Service module 36403: business logic, no crypto."""


def calculate_total_36403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36403():
    return 'module 36403 handles orders and invoices'
