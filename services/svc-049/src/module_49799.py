"""Service module 49799: business logic, no crypto."""


def calculate_total_49799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49799():
    return 'module 49799 handles orders and invoices'
