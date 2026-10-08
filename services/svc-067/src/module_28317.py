"""Service module 28317: business logic, no crypto."""


def calculate_total_28317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28317():
    return 'module 28317 handles orders and invoices'
