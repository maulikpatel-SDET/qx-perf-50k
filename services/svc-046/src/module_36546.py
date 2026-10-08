"""Service module 36546: business logic, no crypto."""


def calculate_total_36546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36546():
    return 'module 36546 handles orders and invoices'
