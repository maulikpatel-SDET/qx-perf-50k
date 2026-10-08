"""Service module 28486: business logic, no crypto."""


def calculate_total_28486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28486():
    return 'module 28486 handles orders and invoices'
