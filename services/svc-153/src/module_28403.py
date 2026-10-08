"""Service module 28403: business logic, no crypto."""


def calculate_total_28403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28403():
    return 'module 28403 handles orders and invoices'
