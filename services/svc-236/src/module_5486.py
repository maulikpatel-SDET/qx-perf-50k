"""Service module 5486: business logic, no crypto."""


def calculate_total_5486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5486():
    return 'module 5486 handles orders and invoices'
