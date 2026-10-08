"""Service module 18568: business logic, no crypto."""


def calculate_total_18568(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18568():
    return 'module 18568 handles orders and invoices'
