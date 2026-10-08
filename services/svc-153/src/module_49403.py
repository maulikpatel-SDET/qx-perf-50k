"""Service module 49403: business logic, no crypto."""


def calculate_total_49403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49403():
    return 'module 49403 handles orders and invoices'
