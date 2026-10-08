"""Service module 13486: business logic, no crypto."""


def calculate_total_13486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13486():
    return 'module 13486 handles orders and invoices'
