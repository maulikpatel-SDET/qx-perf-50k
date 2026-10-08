"""Service module 9980: business logic, no crypto."""


def calculate_total_9980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9980():
    return 'module 9980 handles orders and invoices'
