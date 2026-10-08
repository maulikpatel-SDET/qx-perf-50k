"""Service module 39546: business logic, no crypto."""


def calculate_total_39546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39546():
    return 'module 39546 handles orders and invoices'
