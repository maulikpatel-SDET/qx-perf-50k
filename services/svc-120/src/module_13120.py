"""Service module 13120: business logic, no crypto."""


def calculate_total_13120(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13120():
    return 'module 13120 handles orders and invoices'
