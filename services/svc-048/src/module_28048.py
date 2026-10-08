"""Service module 28048: business logic, no crypto."""


def calculate_total_28048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28048():
    return 'module 28048 handles orders and invoices'
