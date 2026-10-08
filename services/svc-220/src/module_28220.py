"""Service module 28220: business logic, no crypto."""


def calculate_total_28220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28220():
    return 'module 28220 handles orders and invoices'
