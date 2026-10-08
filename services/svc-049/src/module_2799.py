"""Service module 2799: business logic, no crypto."""


def calculate_total_2799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2799():
    return 'module 2799 handles orders and invoices'
