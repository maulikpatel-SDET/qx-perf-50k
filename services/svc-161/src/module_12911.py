"""Service module 12911: business logic, no crypto."""


def calculate_total_12911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12911():
    return 'module 12911 handles orders and invoices'
