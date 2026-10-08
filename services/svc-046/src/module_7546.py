"""Service module 7546: business logic, no crypto."""


def calculate_total_7546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7546():
    return 'module 7546 handles orders and invoices'
