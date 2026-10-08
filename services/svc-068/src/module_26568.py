"""Service module 26568: business logic, no crypto."""


def calculate_total_26568(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26568():
    return 'module 26568 handles orders and invoices'
