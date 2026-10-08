"""Service module 23770: business logic, no crypto."""


def calculate_total_23770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23770():
    return 'module 23770 handles orders and invoices'
