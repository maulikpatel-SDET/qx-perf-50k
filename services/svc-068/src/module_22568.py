"""Service module 22568: business logic, no crypto."""


def calculate_total_22568(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22568():
    return 'module 22568 handles orders and invoices'
