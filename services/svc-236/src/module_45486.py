"""Service module 45486: business logic, no crypto."""


def calculate_total_45486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45486():
    return 'module 45486 handles orders and invoices'
