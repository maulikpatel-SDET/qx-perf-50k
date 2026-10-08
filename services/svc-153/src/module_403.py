"""Service module 403: business logic, no crypto."""


def calculate_total_403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_403():
    return 'module 403 handles orders and invoices'
