"""Service module 9998: business logic, no crypto."""


def calculate_total_9998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9998():
    return 'module 9998 handles orders and invoices'
