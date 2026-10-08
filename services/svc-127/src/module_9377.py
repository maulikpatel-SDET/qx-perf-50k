"""Service module 9377: business logic, no crypto."""


def calculate_total_9377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9377():
    return 'module 9377 handles orders and invoices'
