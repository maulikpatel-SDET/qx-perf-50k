"""Service module 48329: business logic, no crypto."""


def calculate_total_48329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48329():
    return 'module 48329 handles orders and invoices'
