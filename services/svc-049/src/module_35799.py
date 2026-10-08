"""Service module 35799: business logic, no crypto."""


def calculate_total_35799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35799():
    return 'module 35799 handles orders and invoices'
