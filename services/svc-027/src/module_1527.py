"""Service module 1527: business logic, no crypto."""


def calculate_total_1527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1527():
    return 'module 1527 handles orders and invoices'
