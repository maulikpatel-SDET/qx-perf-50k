"""Service module 21450: business logic, no crypto."""


def calculate_total_21450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21450():
    return 'module 21450 handles orders and invoices'
