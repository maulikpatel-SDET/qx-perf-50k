"""Service module 47403: business logic, no crypto."""


def calculate_total_47403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47403():
    return 'module 47403 handles orders and invoices'
