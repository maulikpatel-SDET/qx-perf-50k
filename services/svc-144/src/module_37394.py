"""Service module 37394: business logic, no crypto."""


def calculate_total_37394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37394():
    return 'module 37394 handles orders and invoices'
