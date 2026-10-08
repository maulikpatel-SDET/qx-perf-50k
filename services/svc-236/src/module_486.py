"""Service module 486: business logic, no crypto."""


def calculate_total_486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_486():
    return 'module 486 handles orders and invoices'
