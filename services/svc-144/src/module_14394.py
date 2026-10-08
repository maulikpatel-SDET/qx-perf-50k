"""Service module 14394: business logic, no crypto."""


def calculate_total_14394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14394():
    return 'module 14394 handles orders and invoices'
