"""Service module 14461: business logic, no crypto."""


def calculate_total_14461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14461():
    return 'module 14461 handles orders and invoices'
