"""Service module 11140: business logic, no crypto."""


def calculate_total_11140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11140():
    return 'module 11140 handles orders and invoices'
