"""Service module 12192: business logic, no crypto."""


def calculate_total_12192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12192():
    return 'module 12192 handles orders and invoices'
