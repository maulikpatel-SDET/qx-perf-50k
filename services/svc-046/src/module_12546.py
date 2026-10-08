"""Service module 12546: business logic, no crypto."""


def calculate_total_12546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12546():
    return 'module 12546 handles orders and invoices'
