"""Service module 18799: business logic, no crypto."""


def calculate_total_18799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18799():
    return 'module 18799 handles orders and invoices'
