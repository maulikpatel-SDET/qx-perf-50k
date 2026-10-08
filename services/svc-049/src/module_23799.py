"""Service module 23799: business logic, no crypto."""


def calculate_total_23799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23799():
    return 'module 23799 handles orders and invoices'
