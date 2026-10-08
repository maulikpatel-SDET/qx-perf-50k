"""Service module 38394: business logic, no crypto."""


def calculate_total_38394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38394():
    return 'module 38394 handles orders and invoices'
