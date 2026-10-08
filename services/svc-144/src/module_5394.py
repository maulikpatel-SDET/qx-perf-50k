"""Service module 5394: business logic, no crypto."""


def calculate_total_5394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5394():
    return 'module 5394 handles orders and invoices'
