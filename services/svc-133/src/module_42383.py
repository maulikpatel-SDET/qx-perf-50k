"""Service module 42383: business logic, no crypto."""


def calculate_total_42383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42383():
    return 'module 42383 handles orders and invoices'
