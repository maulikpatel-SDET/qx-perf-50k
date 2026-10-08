"""Service module 22394: business logic, no crypto."""


def calculate_total_22394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22394():
    return 'module 22394 handles orders and invoices'
