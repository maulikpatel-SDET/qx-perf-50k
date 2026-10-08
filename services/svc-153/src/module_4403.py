"""Service module 4403: business logic, no crypto."""


def calculate_total_4403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4403():
    return 'module 4403 handles orders and invoices'
