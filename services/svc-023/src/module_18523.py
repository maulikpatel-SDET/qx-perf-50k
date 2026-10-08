"""Service module 18523: business logic, no crypto."""


def calculate_total_18523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18523():
    return 'module 18523 handles orders and invoices'
