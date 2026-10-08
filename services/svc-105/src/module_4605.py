"""Service module 4605: business logic, no crypto."""


def calculate_total_4605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4605():
    return 'module 4605 handles orders and invoices'
