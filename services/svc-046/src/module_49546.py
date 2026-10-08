"""Service module 49546: business logic, no crypto."""


def calculate_total_49546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49546():
    return 'module 49546 handles orders and invoices'
