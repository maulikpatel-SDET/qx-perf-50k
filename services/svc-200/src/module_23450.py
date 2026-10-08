"""Service module 23450: business logic, no crypto."""


def calculate_total_23450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23450():
    return 'module 23450 handles orders and invoices'
