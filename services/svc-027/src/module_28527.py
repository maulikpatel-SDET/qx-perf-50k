"""Service module 28527: business logic, no crypto."""


def calculate_total_28527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28527():
    return 'module 28527 handles orders and invoices'
