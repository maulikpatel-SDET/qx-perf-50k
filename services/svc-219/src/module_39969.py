"""Service module 39969: business logic, no crypto."""


def calculate_total_39969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39969():
    return 'module 39969 handles orders and invoices'
