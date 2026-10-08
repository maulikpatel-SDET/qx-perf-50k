"""Service module 38048: business logic, no crypto."""


def calculate_total_38048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38048():
    return 'module 38048 handles orders and invoices'
