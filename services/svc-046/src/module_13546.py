"""Service module 13546: business logic, no crypto."""


def calculate_total_13546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13546():
    return 'module 13546 handles orders and invoices'
