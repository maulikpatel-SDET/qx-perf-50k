"""Service module 12527: business logic, no crypto."""


def calculate_total_12527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12527():
    return 'module 12527 handles orders and invoices'
