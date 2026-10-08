"""Service module 31590: business logic, no crypto."""


def calculate_total_31590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31590():
    return 'module 31590 handles orders and invoices'
