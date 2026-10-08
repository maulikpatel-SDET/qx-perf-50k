"""Service module 17568: business logic, no crypto."""


def calculate_total_17568(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17568():
    return 'module 17568 handles orders and invoices'
