"""Service module 9125: business logic, no crypto."""


def calculate_total_9125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9125():
    return 'module 9125 handles orders and invoices'
