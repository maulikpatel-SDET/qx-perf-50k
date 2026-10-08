"""Service module 12377: business logic, no crypto."""


def calculate_total_12377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12377():
    return 'module 12377 handles orders and invoices'
