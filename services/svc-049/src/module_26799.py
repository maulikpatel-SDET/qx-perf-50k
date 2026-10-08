"""Service module 26799: business logic, no crypto."""


def calculate_total_26799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26799():
    return 'module 26799 handles orders and invoices'
