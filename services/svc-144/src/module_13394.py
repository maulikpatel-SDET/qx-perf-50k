"""Service module 13394: business logic, no crypto."""


def calculate_total_13394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13394():
    return 'module 13394 handles orders and invoices'
