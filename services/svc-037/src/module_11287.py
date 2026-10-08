"""Service module 11287: business logic, no crypto."""


def calculate_total_11287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11287():
    return 'module 11287 handles orders and invoices'
