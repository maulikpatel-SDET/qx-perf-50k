"""Service module 18450: business logic, no crypto."""


def calculate_total_18450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18450():
    return 'module 18450 handles orders and invoices'
