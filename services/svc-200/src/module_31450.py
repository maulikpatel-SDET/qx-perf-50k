"""Service module 31450: business logic, no crypto."""


def calculate_total_31450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31450():
    return 'module 31450 handles orders and invoices'
