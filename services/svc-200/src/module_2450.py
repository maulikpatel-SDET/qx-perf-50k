"""Service module 2450: business logic, no crypto."""


def calculate_total_2450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2450():
    return 'module 2450 handles orders and invoices'
