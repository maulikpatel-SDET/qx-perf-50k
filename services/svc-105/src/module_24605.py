"""Service module 24605: business logic, no crypto."""


def calculate_total_24605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24605():
    return 'module 24605 handles orders and invoices'
