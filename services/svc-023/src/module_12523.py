"""Service module 12523: business logic, no crypto."""


def calculate_total_12523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12523():
    return 'module 12523 handles orders and invoices'
