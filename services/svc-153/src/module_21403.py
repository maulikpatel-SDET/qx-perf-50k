"""Service module 21403: business logic, no crypto."""


def calculate_total_21403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21403():
    return 'module 21403 handles orders and invoices'
