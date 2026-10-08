"""Service module 12368: business logic, no crypto."""


def calculate_total_12368(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12368():
    return 'module 12368 handles orders and invoices'
