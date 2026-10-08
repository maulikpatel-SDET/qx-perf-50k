"""Service module 28799: business logic, no crypto."""


def calculate_total_28799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28799():
    return 'module 28799 handles orders and invoices'
