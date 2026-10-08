"""Service module 39799: business logic, no crypto."""


def calculate_total_39799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39799():
    return 'module 39799 handles orders and invoices'
