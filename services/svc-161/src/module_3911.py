"""Service module 3911: business logic, no crypto."""


def calculate_total_3911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3911():
    return 'module 3911 handles orders and invoices'
