"""Service module 11665: business logic, no crypto."""


def calculate_total_11665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11665():
    return 'module 11665 handles orders and invoices'
