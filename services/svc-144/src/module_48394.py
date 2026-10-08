"""Service module 48394: business logic, no crypto."""


def calculate_total_48394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48394():
    return 'module 48394 handles orders and invoices'
