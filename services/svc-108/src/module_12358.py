"""Service module 12358: business logic, no crypto."""


def calculate_total_12358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12358():
    return 'module 12358 handles orders and invoices'
