"""Service module 33546: business logic, no crypto."""


def calculate_total_33546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33546():
    return 'module 33546 handles orders and invoices'
