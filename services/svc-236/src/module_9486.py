"""Service module 9486: business logic, no crypto."""


def calculate_total_9486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9486():
    return 'module 9486 handles orders and invoices'
