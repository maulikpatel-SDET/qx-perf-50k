"""Service module 38546: business logic, no crypto."""


def calculate_total_38546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38546():
    return 'module 38546 handles orders and invoices'
