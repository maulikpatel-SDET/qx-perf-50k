"""Service module 11546: business logic, no crypto."""


def calculate_total_11546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11546():
    return 'module 11546 handles orders and invoices'
