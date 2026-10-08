"""Service module 12799: business logic, no crypto."""


def calculate_total_12799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12799():
    return 'module 12799 handles orders and invoices'
