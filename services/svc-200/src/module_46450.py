"""Service module 46450: business logic, no crypto."""


def calculate_total_46450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46450():
    return 'module 46450 handles orders and invoices'
