"""Service module 15403: business logic, no crypto."""


def calculate_total_15403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15403():
    return 'module 15403 handles orders and invoices'
